from rest_framework import permissions
from reviews.models import User


class IsAdminOrSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        user = User.objects.get(username=request.user.username)
        return (request.user.is_authenticated
                and (user.role == 'admin' or request.user.is_superuser))


class IsModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        user = User.objects.get(username=request.user.username)
        return (request.user.is_authenticated and user.role == 'moderator')


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                and request.user.is_authenticated
                and request.user.role == 'admin')


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated
                and request.user.role == 'admin'))
