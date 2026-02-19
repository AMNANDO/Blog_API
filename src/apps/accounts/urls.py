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
router = DefaultRouter()
router.register()
urlpatterns = router.urls