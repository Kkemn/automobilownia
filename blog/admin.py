from django.contrib import admin
from .models import Author, Tag, Category, Post

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category', 'title')}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
