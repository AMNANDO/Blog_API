from auth_profile_system.src.apps.accounts.urls import urlpatterns
from .views import *
from rest_framework.routers import DefaultRouter
 router = DefaultRouter()
 router.register()
 urlpatterns = router.urls