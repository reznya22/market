from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from books.models import Review
from books.serializers.api import reviews as reviews_s
from common.permissions import IsAuthorOrStaff


# region api_documentation
@extend_schema_view(
    delete=extend_schema(summary='Удалить отзыв', tags=['Отзывы']),
    get=extend_schema(summary='Получить отзыв', tags=['Отзывы']),
)
# endregion
class ReviewAPIView(generics.RetrieveDestroyAPIView):
    """Get or delete your review"""
    serializer_class = reviews_s.ReviewSerializer
    permission_classes = [IsAuthorOrStaff]

    def get_queryset(self, *args, **kwargs):
        queryset = Review.objects.all()
        return queryset.filter(book_id=self.kwargs['book_pk'])


# region api_documentation
@extend_schema_view(
    create=extend_schema(summary='Создать отзыв', tags=['Отзывы']),
    list=extend_schema(summary='Получить все отзывы к книге', tags=['Отзывы']),
)
# endregion
class CreateReviewViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    """Create review or get list of reviews"""
    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['pk'])

    def get_serializer_class(self):
        if self.action == 'create':
            return reviews_s.CreateReviewSerializer
        return reviews_s.ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(book_id=self.kwargs['pk'], user=self.request.user)
