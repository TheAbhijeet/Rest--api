from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework import permissions

class SafeMethodsOnly(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj=None):
        return request.method in SAFE_METHODS


class AdminOrAuthorCanEdit(BasePermission):

    def has_permission(self, request, view):
        """All users can list or view."""
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj=None):
        """Only the author can modify existing instances."""
        is_safe = request.method in SAFE_METHODS

        try:
            is_author = request.user == obj.author
        except AttributeError:
            is_author = False

        return is_safe or is_author or request.user.is_superuser

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user