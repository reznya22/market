from django.urls import path

from books.views import BookView, OneBookView


urlpatterns = [
    path('books/', BookView.as_view(), name='books'),
    path('book/<int:pk>', OneBookView.as_view(), name="book")
]
