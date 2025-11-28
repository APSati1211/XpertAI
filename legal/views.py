from rest_framework import viewsets
from .models import LegalPage
from .serializers import LegalPageSerializer

class LegalPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LegalPage.objects.all()
    serializer_class = LegalPageSerializer
    lookup_field = 'slug' # URL mein ID ki jagah Slug use karenge (e.g. /api/legal/privacy-policy/)