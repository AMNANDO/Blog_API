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