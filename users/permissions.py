from rest_framework import permissions


class Iscollaborator(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.is_superuser


class IscollaboratorOrReadOnly(Iscollaborator):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or super().has_permission(
            request, view
        )
