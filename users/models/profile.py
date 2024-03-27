from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        to='users.User',
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Пользователь',
        primary_key=True
    )
    telegram_id = models.CharField(
        verbose_name='Telegram ID',
        max_length=20,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return f'{self.user} ({self.pk})'
