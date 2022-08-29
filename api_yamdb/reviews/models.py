from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    CHOICES = [
        (USER, 'User'),
        (ADMIN, 'Administrator'),
        (MODERATOR, 'Moderator'),
    ]
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=100,
        null=True,
        unique=True
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
    )
    bio = models.TextField(
        verbose_name='Биография',
        null=True,
        blank=True
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=50,
        choices=CHOICES,
        default=USER
    )

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Token(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='token',
    )
    token = models.CharField(
        max_length=200,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'token'],
                name='unique_token'
            )
        ]
        verbose_name = 'Код подтверждения'
        verbose_name_plural = 'Коды подтверждения'
