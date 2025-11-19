from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SiteContentViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'sitecontent', SiteContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]