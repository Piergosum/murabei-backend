

from rest_framework import serializers
from .models import Book
from .models import Author
from .models import Subject
from .models import BookSubjects
from .exceptions import InvalidAuthorID


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_author_id(self, value):
        try:
            Author.objects.get(pk=value)
        except Author.DoesNotExist:
            raise InvalidAuthorID()
        return value


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class BookSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSubjects
        fields = '__all__'
