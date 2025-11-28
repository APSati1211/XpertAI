from django.urls import path
from .views import ServicePageDataView

urlpatterns = [
    path('services-page-data/', ServicePageDataView.as_view(), name='services-page-data'),
]