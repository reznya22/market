import pdb

from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.viewsets import ReadOnlyModelViewSet
from books.serializers.api import books as books_s
from books.models import Book, FavoriteBook
from rest_framework.generics import ListCreateAPIView, ListAPIView
from common.permissions import IsAuthorOnly
from rest_framework.permissions import IsAdminUser


# region api_documentation
@extend_schema_view(
     retrieve=extend_schema(summary='Информация о книге', tags=['Книги']),
     list=extend_schema(summary='Список книг', tags=['Книги']),
)
# endregion
class BookViewSet(ReadOnlyModelViewSet):
    """Get one book or list of books"""
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return books_s.BookListSerializer
        return books_s.BookSerializer


# region api_documentation
@extend_schema_view(
     get=extend_schema(
         summary='Получить избранные книги пользователей', tags=['Книги']),
)
# endregion
class FavoriteBookView(ListAPIView):
    """Get list of all users favorite books"""
    queryset = FavoriteBook.objects.all()
    serializer_class = books_s.FavoriteBookSerializer
    permission_classes = [IsAdminUser]


# region api_documentation
@extend_schema_view(
     get=extend_schema(summary='Получить избранные книги', tags=['Книги']),
     create=extend_schema(summary='Добавить избранную книгу', tags=['Книги']),
)
# endregion
class UserFavoriteBookView(ListCreateAPIView):
    """Get list of the user favorite books"""
    serializer_class = books_s.FavoriteBookSerializer
    permission_classes = [IsAuthorOnly]

    def get_queryset(self):
        user_pk = self.request.user.pk
        queryset = FavoriteBook.objects.filter(user=user_pk)
        return queryset
