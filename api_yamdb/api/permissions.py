from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    """
    Разрешено только для автора.
    """

    def has_object_permission(self, request):
        return (
            request.method in permissions.SAFE_METHOD
            or request.author == request.user
        )
