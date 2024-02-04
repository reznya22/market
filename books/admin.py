from django.contrib import admin

from books.models import Book, Review


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
            'book_id', 'title', 'author',
            'publication_year', 'genre', 'ISBN',
            'price', 'image', 'description', 'quantity_on_stock'
            )
