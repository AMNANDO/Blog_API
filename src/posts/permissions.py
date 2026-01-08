from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsPostAuthorOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user or
            request.user.role == 'admin'
        )