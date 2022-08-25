from api.mixins import MyViewSet, UpdateModelMixin
from api.permissions import IsAuthorOrReadOnly
from api.serializers import (CategorySerializer, GenreSerializer,
                             TitleSerializer, ReviewSerializer, CommentSerializer)
from rest_framework import filters, viewsets, mixins
from rest_framework.pagination import LimitOffsetPagination
from yamdb.models import Category, Comments, Genre, Reviews, Title


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


class ReviewCommentViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin,
    mixins.ListModelMixin, mixins.DestroyModelMixin, UpdateModelMixin, 
    viewsets.GenericViewSet):
    pass 


class ReviewViewSet(ReviewCommentViewSet):
    """"""

    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer


class CommentViewSet(ReviewCommentViewSet):
    """"""
    
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer