from rest_framework import permissions

from users.models import User


class IsCollaborator(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.is_superuser


class ItsOwnAccount(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, User):
            return obj == request.user
        return obj.user == request.user




