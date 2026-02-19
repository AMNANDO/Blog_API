from .views import PostViewSet
from rest_framework.routers import DefaultRouter

app_name = "posts"

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')
urlpatterns = router.urls