from math import trunc

from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (CreateAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     ListAPIView)
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated)
from .serializers import (RegisterUserSerializer,
                          UserDetailSerializer,
                          UpdateUserSerializer,
                          UserAdminSerializer)
from .permissions import (IsAdmin,
                          IsSelf)
from .models import User

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

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserAdminSerializer
    permission_classes = [IsAdmin]

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.get()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.user.role == User.ROLE_ADMIN:
            return [IsAdmin()]
        return [IsSelf()]

class ChangeUserRoleView(APIView):
    permission_classes = [IsAdmin]

    def patch(self, request, pk):
        role = request.data.get('role')

        if role not in [User.ROLE_ADMIN, User.ROLE_AUTHOR, User.ROLE_USER]:
            return Response(
                {"detail": "invalid role"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.role = role
        user.save()

        return Response(
            {"id": user.id, "role": user.role},
            status=status.HTTP_200_OK
        )