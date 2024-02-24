from django.db import models
from books.models import Book
from users.models.users import User


class Order(models.Model):
    """Модель заказа"""
    order_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(verbose_name='Пользователь', to=User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(verbose_name='Дата', auto_now=True)
    order_status = models.CharField(verbose_name='Статус', max_length=40, default='Ожидает')
    total_price = models.DecimalField(verbose_name='Цена заказа', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-order_date',)

    def __str__(self):
        return f"order № {self.order_id}"


class OrderItem(models.Model):
    """Модель элемента заказа"""
    order = models.ForeignKey(verbose_name='Заказ', to=Order, on_delete=models.CASCADE)
    book = models.ForeignKey(verbose_name='Книга', to=Book, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество')
    price_at_order = models.DecimalField(verbose_name='Цена в момент заказа', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Элементы заказа'
