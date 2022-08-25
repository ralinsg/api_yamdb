from rest_framework import mixins, viewsets
from rest_framework.exceptions import MethodNotAllowed

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


class UpdateModelMixin(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    """

    def update(self, *args, **kwargs):
        raise MethodNotAllowed("POST", detail="Use PATCH")

    def partial_update(self, request, *args, **kwargs):
        # Override Partial Update Code if desired
        return super().update(*args, **kwargs, partial=True)
