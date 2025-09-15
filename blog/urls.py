from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post'),
    path('author/<slug:author>/', views.AuthorListView.as_view(), name='author-posts'),
    path('category/<slug:category>/', views.CategoryListView.as_view(), name='category'),
    path('tag/<slug:tag>', views.TagListView.as_view(), name='tag'),
    path('search/', views.SearchResultsView.as_view(), name='search_post'),
]