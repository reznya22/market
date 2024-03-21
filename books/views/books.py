from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.viewsets import ReadOnlyModelViewSet
from books.serializers.api import books as books_s
from books.models import Book


@extend_schema_view(
     retrieve=extend_schema(summary='Информация о книге', tags=['Книги']),
     list=extend_schema(summary='Список книг', tags=['Книги']),
)
class BookViewSet(ReadOnlyModelViewSet):
    """Get one book or list of books"""
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return books_s.BookListSerializer
        return books_s.BookSerializer
