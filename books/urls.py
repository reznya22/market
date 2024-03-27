from django.urls import path
from books.views.reviews import ReviewAPIView, CreateReviewViewSet
from books.views.books import (
    BookViewSet,
    FavoriteBookView,
    UserFavoriteBookView
)

urlpatterns = [
    # books
    path('books/', BookViewSet.as_view(
        {'get': 'list'}), name='books'),
    path('books/<int:pk>/', BookViewSet.as_view(
        {'get': 'retrieve'}), name='book'),
    path('books/favorite/', FavoriteBookView.as_view(), name='favorite'),
    path('books/my-favorite/', UserFavoriteBookView.as_view(),
         name='user_favorite'),
    # reviews
    path('books/<int:pk>/reviews/', CreateReviewViewSet.as_view({
         'get': 'list',
         'post': 'create'}), name='reviews'),
    path('books/<int:book_pk>/reviews/<int:pk>/', ReviewAPIView.as_view(),
         name='review'),



]
