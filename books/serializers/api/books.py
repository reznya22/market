from rest_framework import serializers
from books.models import Book, FavoriteBook
from books.serializers.api import reviews


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
    reviews = reviews.ReviewSerializer(many=True)

    class Meta:
        model = Book
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


class FavoriteBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoriteBook
        fields = (
            'book',
            'user',
        )
        read_only_fields = (
            'user',
        )

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        obj = FavoriteBook.objects.create(**validated_data)
        return obj

