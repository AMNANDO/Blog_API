from .views import PostLikeView, PostLikesListView
from django.urls import path
from rest_framework.routers import DefaultRouter

app_name = 'likes'

urlpatterns = [
    path("posts/<int:psot_id>/like/", PostLikeView.as_view(), name='post-like'),
    path("post/<int:pk>/likes/", PostLikesListView.as_view(), name='post-likes'),
]