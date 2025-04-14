from django.db import models
from datetime import date

class Author(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name
    
class Category(models.Model):
    title = models.CharField()
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    tags = models.ManyToManyField(Tag)
    published_date = models.DateField(default=date.today)
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f'{self.category}: {self.title}'
    



