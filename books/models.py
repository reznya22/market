from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg

from common.models.mixins import InfoMixin

User = get_user_model()


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Жанр',
        max_length=50
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Book(InfoMixin):
    book_id = models.AutoField(
        primary_key=True
    )
    title = models.CharField(
        verbose_name='Название',
        max_length=100
    )
    author = models.CharField(
        verbose_name='Автор',
        max_length=100
    )
    publication_year = models.PositiveIntegerField(
        verbose_name='Год публикации',
        blank=True
    )
    genre = models.ForeignKey(
        to=Genre,
        on_delete=models.CASCADE
    )
    ISBN = models.PositiveBigIntegerField(
        verbose_name='ISBN',
        unique=True,
        blank=True
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=5,
        decimal_places=2,
        null=True
    )
    image = models.ImageField(
        verbose_name='Обложка',
        upload_to='%Y/%m/%d'
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=500,
        blank=True
    )
    quantity_on_stock = models.PositiveIntegerField(
        verbose_name='Кол-во на складе',
        default=0
    )

    @property
    def rating(self):
        return self.reviews.aggregate(
            avg_rating=Avg('rating'))['avg_rating']

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ('-title',)

    def __str__(self):
        return self.title


class FavoriteBook(models.Model):
    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Избранные книги'
        verbose_name = 'Избранные книги'
        unique_together = (('book', 'user'),)

    def __str__(self):
        return {f"{self.user} favorite book {self.book}"}


class Review(models.Model):
    review_id = models.AutoField(
        primary_key=True
    )
    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    rating = models.FloatField(
        verbose_name='Рейтинг',
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0)]
    )
    review_text = models.TextField(
        verbose_name='Текст отзыва',
        max_length=500
    )
    date = models.DateTimeField(
        verbose_name='Дата',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-date',)
        unique_together = (('book', 'user'),)

    def __str__(self):
        return f'review №{self.pk} user №{self.user}'

