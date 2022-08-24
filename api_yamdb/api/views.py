from api.mixins import MyViewSet
from api.permissions import IsAuthorOrReadOnly
from api.serializers import (CategorySerializer, GenreSerializer,
                             TitleSerializer)
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from yamdb.models import Category, Genre, Title


class CategoryViewSet(MyViewSet):

    """Получение списка всех категорий.
    Добавление новых категорий.
    Удаление категорий.
    Поиск по названию категорий.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permissions_classes = (IsAuthorOrReadOnly, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )


class GenreViewSet(MyViewSet):

    """Получение списка всех жанров.
    Добавление жанров.
    Удаление жанров.
    """

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permissions_classes = (IsAuthorOrReadOnly, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )


class TitleViewSet(viewsets.ModelViewSet):

    """Получение списка всех произведений.
    Добавление произведений.
    Получение информации о произведении.
    Частисное обновление информации о произведении.
    Удаление произведения.
    """

    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('category', 'genre', 'name', 'year', )
    pagination_class = LimitOffsetPagination
