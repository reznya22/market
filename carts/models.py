from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum

from books.models import Book
from common.models.mixins import DateMixin

User = get_user_model()


class CartItem(models.Model):
    cart = models.ForeignKey(
        verbose_name='Корзина',
        to='Cart',
        on_delete=models.CASCADE,
        related_name='cart_items'
    )
    book = models.ForeignKey(
        verbose_name='Книга',
        to=Book,
        on_delete=models.CASCADE,
        related_name='books'
    )

    class Meta:
        verbose_name = 'Элементы заказа'
        verbose_name_plural = 'Элементы заказа'

    def __str__(self):
        return f"book {self.book}, cart {self.cart}"


class Cart(DateMixin):
    user = models.OneToOneField(
        verbose_name='Пользователь',
        to=User,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
        ordering = ('-updated_at',)


class Order(models.Model):
    cart = models.OneToOneField(
        verbose_name='Корзина',
        to='Cart',
        on_delete=models.CASCADE,
    )
    order_date = models.DateTimeField(
        verbose_name='Дата',
        auto_now=True
    )
    order_status = models.CharField(
        verbose_name='Статус',
        max_length=40,
        default='Ожидает'
    )
    total_price = models.DecimalField(
        verbose_name='Цена заказа',
        max_digits=8,
        decimal_places=2,
        default=0
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-order_date',)

    def __str__(self):
        return f"order {self.order_date}"
