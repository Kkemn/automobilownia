from django.contrib import admin
from .models import Author, Tag, Category, Post

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category', 'title')}

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post)
