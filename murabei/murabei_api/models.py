
from django.db import models


class Author(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    biography = models.TextField()

    def __str__(self):
        return self.title


class Subject(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.TextField(name='title')
    author_id = models.IntegerField(name='author_id')
    title_slug = models.TextField(unique=True, name='title_slug')
    price = models.TextField(name='price')
    format = models.TextField(name='format')
    publisher = models.TextField(name='publisher')
    pubdate = models.TextField(name='pubdate')
    edition = models.TextField(name='edition')
    lexile = models.TextField(name='lexile')
    pages = models.FloatField(name='pages')
    dimensions = models.TextField(name='dimensions')
    overview = models.TextField(name='overview')
    excerpt = models.TextField(name='excerpt')
    synopsis = models.TextField(name='synopsis')
    toc = models.TextField(name='toc')
    editorial_reviews = models.TextField(name='editorial_reviews')

    def __str__(self):
        return self.title


class BookSubjects(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, default=None)
