from rest_framework import serializers
from books.models import Book
from books.serializers.nested import reviews


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'book_id',
            'title',
            'author',
            'publication_year',
            'genre',
            'price',
            'image',
            'rating',
            )


class BookSerializer(serializers.ModelSerializer):
    reviews = reviews.ReviewListSerializer(many=True)

    class Meta:
        fields = (
            'book_id',
            'title',
            'author',
            'publication_year',
            'genre',
            'price',
            'ISBN',
            'description',
            'quantity_on_stock',
            'image',
            'rating',
            'reviews',
        )
        model = Book
