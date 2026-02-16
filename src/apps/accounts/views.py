from django.shortcuts import render
from django.contrib.auth import get_user_model
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