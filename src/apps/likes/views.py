from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404

from posts.models import Post
from .models import Like
from .serializers import LikeSerializer, LikeCreateSerializer
from .permissions import CanLikePost

# Create your views here.

class PostLikeView(APIView):

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def post(self, request, post_id):

        post = self.get_post()

        if not post.is_active or post.status != 'published':
            return Response(
                {"detail": "cannot like this post"},
                status=status.HTTP_403_FORBIDDEN
            )

        if Like.objects.filter(post=post, user=request.user).exists():
            return Response(
                {"detail": "You already liked this post"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = LikeSerializer(
            data={},
            context={'request': request, 'post': post}
        )

        serializer.is_valid(raise_exception=True)
        like = serializer.save()

        return Response(
            LikeSerializer(like).data,
            status=status.HTTP_201_CREATED
        )

    def delete(self, request, post_id):

        post = self.get_post()

        try:
            like = Like.objects.get(post=post, user=request.user)
        except Like.DoesNotExist:
            return Response(
                {"detail": "You have not liked this post"},
                status=status.HTTP_400_FORBIDDEN
            )

        like.delete()

        return Response(
            {"detail": "like removed successfully"},
            status=status.HTTP_204_NO_CONTENT
        )

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), CanLikePost()]
        if self.request.method == "DELETE":
            return [IsAuthenticated()]
        return [AllowAny()]