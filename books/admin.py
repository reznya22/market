from django.contrib import admin

from books.models import Book, Review


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
            'title', 'author',
            'publication_year', 'genre', 'ISBN',
            'price', 'image', 'description', 'quantity_on_stock'
            )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_text',)
