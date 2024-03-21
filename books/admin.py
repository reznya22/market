from django.contrib import admin

from books.models import Book, Review, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
            'book_id', 'title', 'author',
            'publication_year', 'genre', 'ISBN',
            'price', 'quantity_on_stock'
            )
    list_display_links = ('title', 'ISBN', 'author',)
    search_fields = ('title', 'author', 'ISBN',)
    readonly_fields = (
        'created_at', 'updated_at',
        'created_by', 'updated_by',
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'review_text', 'date')
    list_display_links = ('book', 'user', 'review_text', 'date',)

    search_fields = ('book', 'user', 'date',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)

    search_fields = ('id', 'name',)
