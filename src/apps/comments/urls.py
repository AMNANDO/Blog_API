from .views import PostCommentView, CommentDetailView
from django.urls import path
from rest_framework.routers import DefaultRouter

app_name = "comments"

urlpatterns = [
    path("posts/<int:psot_id>/comments/", PostCommentView.as_view(), name='post-comments'),
    path("<int:pk>", CommentDetailView.as_view(), name='comment-detail'),
]