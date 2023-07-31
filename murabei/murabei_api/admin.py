from django.contrib import admin
from .models import Author
from .models import Book
from .models import Subject
from .models import BookSubjects

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Subject)
admin.site.register(BookSubjects)
