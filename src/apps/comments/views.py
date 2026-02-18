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