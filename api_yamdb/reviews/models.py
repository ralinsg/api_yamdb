from django.contrib.auth.models import AbstractUser
from django.db import models
from reviews.validators import validate_year


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


class Category(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Уникальное имя'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Уникальное имя'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
        validators=[validate_year]
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг',
        null=True,
        default=None
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='genres',
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Категория',
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведение'
