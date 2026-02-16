from django.shortcuts import render
from rest_framework.generics import (CreateAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated)
from .serializers import (RegisterUserSerializer,
                          UserDetailSerializer,
                          UpdateUserSerializer)

# Create your views here.

class RegisterUserView(CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]

class MeView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class UpdateMeView(UpdateAPIView):
    serializer_class = UpdateUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user