from rest_framework import mixins, viewsets


class MyViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    """Возвращает существующий экземпляр можели.
    Создает и сохраняет новые экземпляры модели.
    Удаляет текущий экземпляр модели.
    """
    pass
