from rest_framework import permissions
from rest_framework import status

from .exceptions import CustomValidator


class AdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_authenticated:
            return request.user.role == 'admin'
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return request.user.role == 'admin'
        return False


class ModeratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        if request.user.is_authenticated:
            return (
                obj.author == request.user
                or request.user.role == ('admin' or 'moder')
            )
        return False


class IsAuthorAdminModeratorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'POST':
            return request.user.is_authenticated

        return request.user.is_authenticated and (
                    request.user == obj.author or
                    request.user.is_moderator or
                    request.user.is_admin
            )


class UserOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
                request.user.is_user
                or request.user.is_admin
        )


class IsAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_admin
        raise CustomValidator("Вы не авторизованы", 'token', status.HTTP_401_UNAUTHORIZED)

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return request.user.is_admin
        raise CustomValidator("Вы не авторизованы", 'token', status.HTTP_401_UNAUTHORIZED)
