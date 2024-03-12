from rest_framework import generics
from books.serializers import BookSerializer
from books.models import Book


class BookView(generics.ListAPIView):
    """Get book list"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class OneBookView(generics.RetrieveAPIView, BookView):
    """Get one book"""


