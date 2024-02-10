from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class User(models.Model):
    """Модель пользователя"""
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    phone = PhoneNumberField(verbose_name='Телефон', blank=True, null=True)
    email = models.EmailField(verbose_name='Почта')
    telegram_id = models.PositiveIntegerField(verbose_name='Телеграм', blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
