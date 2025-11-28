from rest_framework.routers import DefaultRouter
from .views import LegalPageViewSet

router = DefaultRouter()
router.register(r'pages', LegalPageViewSet, basename='legal-page')

urlpatterns = router.urls
