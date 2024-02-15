from django.contrib import admin

from books.models import Book, Review


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
            'title', 'author',
            'publication_year', 'genre', 'ISBN',
            'price', 'quantity_on_stock'
            )
    list_display_links = ('title', 'ISBN', 'author',)

    search_fields = ('title', 'author', 'ISBN',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'review_text', 'data')
    list_display_links = ('book', 'user', 'review_text', 'data',)

    search_fields = ('book', 'user', 'data',)
