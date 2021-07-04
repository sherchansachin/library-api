from django.db import models
# serializers help translate the data into the format which is easy to consume over the internet. Eg. JSON format

from rest_framework import serializers
from books.models import Book



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn')