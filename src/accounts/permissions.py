from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    message = 'You don`t have admin access!!'
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role == 'admin'
        )

class IsAuthor(BasePermission):
    message = "Your not Author!!"
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role == 'author'
        )
class IsNormalUser(BasePermission):
    message = 'Your not User!!'
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role == 'user'
        )

class CanModerateContent(BasePermission):
    message = 'You can`t moderate content!!'
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role == 'admin'
        )

class IsSelf(BasePermission):
    message = 'You don`t own this account!!'
    def has_object_permission(self, request, view, obj):
        return obj == request.user

class ReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
