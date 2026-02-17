from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from .models import Post
from .serializers import (
    PostSerializer,
    PostCreateSerializer,
    PostUpdateSerializer,
    PostDetailSerializer,
    PostAdminSerializer
)
from .permissions import (IsPostAuthorOrAdmin,
                          IsPublished,
                          IsActive,
                          CanCreatePost,
                          CanEditPost)

# Create your views here.

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):

        if self.action == 'create':
            return PostCreateSerializer

        if self.action in ['update', 'partial_update']:
            return PostUpdateSerializer

        if self.action == 'retrieve':
            if self.request.user.is_authenticated and self.request.user.role == 'admin':
                return PostAdminSerializer
            return PostDetailSerializer

        return PostSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated and user.role == 'admin':
            return Post.objects.all()

        if user.is_authenticated:
            return Post.objects.filter(
                Q(author=user)|
                Q(status='published', is_active=True)
            )

        return Post.objects.filter(
            status='published',
            is_active=True
        )

    def get_permissions(self):

        if self.action == 'create':
            return [IsAuthenticated(), CanCreatePost()]

        if self.action in ['update', 'partial_update']:
            return (IsAuthenticated(), CanEditPost())

        if self.action == 'destroy':
            return [IsAuthenticated(), IsPostAuthorOrAdmin()]

        if self.action == 'publish':
            return [IsAuthenticated(), IsPostAuthorOrAdmin()]

        return [AllowAny()]

    def destroy(self, request, *args, **kwargs):
         post = self.get_object()
         post.is_active = False
         post.save()
         return Response(
             {"detail": "Post deactivated successfully"},
             status=status.HTTP_204_NO_CONTENT
         )

    @action(detail=True, methods=['patch'])
    def publish(self, request, pk=None):
        post = self.get_object()

        if post.status == Post.STATUS_PUBLISHED:
            return Response(
                {"detail": "Post already published"},
                status=status.HTTP_400_BAD_REQUEST
            )

        post.status = Post.STATUS_PUBLISHED
        post.save()

        return Response(
            {"detail": "Post published successfully"},
            status=status.HTTP_200_OK
        )