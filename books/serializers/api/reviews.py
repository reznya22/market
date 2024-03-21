from rest_framework import serializers
from books.models import Review, Book


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Review
        fields = (
            'review_id',
            'user',
            'username',
            'rating',
            'review_text',
            'date',
        )


class CreateReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = (
            'user',
            'book',
        )


