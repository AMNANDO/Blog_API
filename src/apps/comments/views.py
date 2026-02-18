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
