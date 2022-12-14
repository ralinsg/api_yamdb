from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS
                or request.user.is_authenticated):
            return True
        return False


class IsAdminOrSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and (request.user.is_admin
                     or request.user.is_superuser))


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and request.user.is_moderator)


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                and request.user.is_authenticated
                and request.user.is_admin)


class IsAuthorOrAdminOrModeratorOrReadOnly(permissions.BasePermission):
    """
    Добавлять отзывы и комментарии может только авторизованный пользователь.
    Удалять и изменять отзывы и комментарии могут только автор, модератор
    или администратор.
    Для неавторизованных пользователей доступ только на чтение.
    """

    def has_permission(self, request, view):
        if (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        ):
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            obj.author == request.user
            or request.user.is_admin
            or request.user.is_moderator
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated
                    and request.user.is_admin))


class IsAdminOrModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            and (request.user.is_moderator
                 or request.user.is_admin))
