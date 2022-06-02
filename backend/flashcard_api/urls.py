from .views import NounViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('noun', NounViewSet)
urlpatterns = router.urls