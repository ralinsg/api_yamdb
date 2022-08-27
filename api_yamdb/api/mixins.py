from rest_framework import mixins, viewsets


class MyViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):

    """Возвращает существующий экземпляр можели.
    Создает и сохраняет новые экземпляры модели.
    Удаляет текущий экземпляр модели.
    """

    pass
