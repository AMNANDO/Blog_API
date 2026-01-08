from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsCommentOwner(BasePermission):
    message = 'You don`t own this Comment!!'
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class IsCommentActive(BasePermission):
    message = 'can`t show this Comment!!'
    def has_object_permission(self, request, view, obj):
        return obj.is_active

class CanCreateComments(BasePermission):
    message = 'You can`t create comment!!'
    def has_permission(self, request, view):
        post = view.get_post()
        return (
            request.user.is_authenticated and
            post.is_active and
            post.status == 'published'
        )

class CanEditComments(BasePermission):
    message = 'You can`t edit this comment!!'
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

