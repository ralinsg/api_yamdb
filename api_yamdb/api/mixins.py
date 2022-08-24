from rest_framework import mixins, viewsets


class MyViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    """Возвращает существующий экземпляр можели.
    Создает и сохраняет новые экземпляры модели.
    Удаляет текущий экземпляр модели.
    """
    pass
