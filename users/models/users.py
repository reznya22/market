from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

from users.managers import CustomUserManager
from users.models.profile import Profile


class User(AbstractUser):
    username = models.CharField(
        verbose_name='Никнейм',
        max_length=64,
        unique=True,
        null=True,
        blank=True
    )
    email = models.EmailField(
        verbose_name='Почта',
        unique=True,
    )
    phone_number = PhoneNumberField(
        verbose_name='Телефон',
        unique=True,
        null=True,
        blank=True
    )
    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def full_name(self):
        if self.last_name or self.first_name:
            return f"{self.last_name} {self.first_name}"
        return self.username

    def __str__(self):
        return f"{self.full_name} id{self.pk}"


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)
