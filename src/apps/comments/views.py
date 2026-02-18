from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404

from posts.modles import Post
from .models import Comment
from .serializers import (CommentSerializer,
                          CommentCreateSerializer)
from .permissions import (CanCreateComments,
                          CanEditComment,
                          IsCommentActive,
                          IsCommentOwner)

# Create your views here.

class PostCommentView(APIView):

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def get(self, request, post_id):

        post = self.get_post()

        if not post.is_active or post.status != 'published':
            return Response(
                {"detail": "Post not available"},
                status=status.HTTP_404_NOT_FOUND
            )

        comments = post.comments.filter(is_active=True)
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)

    def post(self, request, post_id):

        post = self.get_post()

        serializer = CommentCreateSerializer(
            data=request.data,
            context={'request': request, 'post': post}
        )

        serializer.is_valid(raise_exception=True)
        comment = serializer.save()

        return Response(
            CommentSerializer(comment).data,
            status=status.HTTP_201_CREATED
                        )
    def get_permissions(self):

        if self.request.method == 'POST':
            return [IsAuthenticated(), CanCreateComments()]

        return [AllowAny()]

class CommentDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):

        if self.request.method == 'GET':
            return [IsCommentActive()]

        if self.request.method in ['PATCH', 'PUT']:
            return [IsAuthenticated(), CanEditComment()]

        if self.request.method == 'DELETE':
            return [IsAuthenticated(), IsCommentOwner()]

        return super().get_permissions()

    def destroy(self, request, *args, **kwargs):

        comment = self.get_object()
        comment.is_active = False
        comment.save()

        return Response(
            {"detail": "Comment deactivated successfully."},
            status=status.HTTP_204_NO_CONTENT
        )
