from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()


class Book(models.Model):
    book_id = models.PositiveIntegerField(verbose_name='id Книги', primary_key=True)
    title = models.CharField(verbose_name='Название', max_length=100)
    author = models.CharField(verbose_name='Автор', max_length=100)
    publication_year = models.PositiveIntegerField('Год публикации', blank=True)
    genre = models.CharField(verbose_name='Жанр', max_length=100)
    ISBN = models.PositiveBigIntegerField(verbose_name='ISBN', unique=True, blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=5, decimal_places=2, null=True)
    image = models.ImageField('Обложка', upload_to='images/')
    description = models.TextField(verbose_name='Описание', max_length=500, blank=True)
    quantity_on_stock = models.PositiveIntegerField(verbose_name='Кол-во на складе', default=0)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ('-title',)

    def __str__(self):
        return f'{self.title} id {self.pk}'


class Review(models.Model):
    review_id = models.PositiveIntegerField('id Отзыва', primary_key=True)
    book = models.OneToOneField(
        to=Book, on_delete=models.CASCADE
    )
    user = models.OneToOneField(
        to=User, on_delete=models.CASCADE
    )
    rating = models.FloatField(
        verbose_name='Автор',
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    review_text = models.TextField(verbose_name='Текст отзыва', max_length=500)
    data = models.DateField(verbose_name='Дата', auto_now=True)

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'
        ordering = ('-data',)

    def __str__(self):
        return f'review {self.pk}'
