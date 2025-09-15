from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Post, Author, Category, Tag

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post.html'

class AuthorListView(ListView):
    model = Post
    template_name = 'blog/author.html'
    paginate_by = 5

    def get_queryset(self):
        self.author = get_object_or_404(Author, slug=self.kwargs['author'])
        return Post.objects.filter(author=self.author, published_at__lte=timezone.now()).order_by('-published_at')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        return context

class CategoryListView(ListView):
    model = Post
    template_name = 'blog/category.html'
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        self.category = get_object_or_404(Category, slug=self.kwargs['category'])
        return Post.objects.filter(category=self.category, published_at__lte=timezone.now()).order_by('published_at')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

class TagListView(ListView):
    model = Post
    template_name = 'blog/tag.html'
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        self.tag = get_object_or_404(Tag, slug=self.kwargs['tag'])
        return Post.objects.filter(tags=self.tag, published_at__lte=timezone.now()).order_by('published_at')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context
    
class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(Q(title__icontains=query) | Q(text__icontains=query), published_at__lte=timezone.now()).order_by('-published_at')
        return Post.objects.none()
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
