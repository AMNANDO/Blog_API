from rest_framework.permissions import BasePermission, SAFE_METHODS

class CanLikePost(BasePermission):
    def has_permission(self, request, view):
        post = view.get_post()
        return (
            request.user.is_authenticated and
            post.is_active and
            post.status == 'published' and
            not post.likes.filter(user=request.user).exists()
        )
