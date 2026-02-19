from auth_profile_system.src.apps.accounts.urls import urlpatterns
from .views import (
    RegisterUserView,
    MeView,
    UpdateMeView,
    UserListView,
    UserDetailView,
    ChangeUserRoleView,
    ToggleUserActiveView
)
from django.urls import path
from rest_framework.routers import DefaultRouter

app_name = "accounts"

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('me/', MeView.as_view(), name='me'),
    path("me/update/", UpdateMeView.as_view(), name='update-me'),

    path("", UserListView.as_view(), name='user-list'),
    path("<int:pk>/", UserDetailView.as_view(), name='user-detail'),
    path("<int:pk>/change-role/", ChangeUserRoleView.as_view(), name='change-user-role'),
    path("<int:pk>/toggle-active/", ToggleUserActiveView.as_view(), name='toggle-user-active'),
]
router = DefaultRouter()
router.register()
urlpatterns = router.urls