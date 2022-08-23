from api.models import Categories, Generes, Titles
from rest_framework import viewsets


class Categories(viewset.ModelViewSet):

    """Получение списка всех категорий.
    Добавление новых категорий.
    Удаление категорий
    """
    queryset = Categories.objects.all()


class Generes(viewset.ModelViewSet):

    """Получение списка всех жанров.
    Добавление жанров.
    Удаление жанров.
    """


class Titles(viewset.ModelViewSet):

    """Получение списка всех произведений.
    Добавление произведений.
    Получение информации о произведении.
    Частисное обновление информации о произведении.
    Удаление произведения.
    """
