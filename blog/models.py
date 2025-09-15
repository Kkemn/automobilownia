from django.db import models
from django.utils.text import slugify

class Author(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100) 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    published_at = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.category}: {self.title}'
    



