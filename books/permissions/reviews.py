from rest_framework.permissions import BasePermission


class ReviewRetrieveDestroyPermission(BasePermission):
    """If user is an author or staff/superuser"""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user
                or request.user.is_superuser
                or request.user.is_staff)
