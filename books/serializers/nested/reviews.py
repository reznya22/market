from rest_framework import serializers
from books.models import Review


class ReviewListSerializer(serializers.ModelSerializer):
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
