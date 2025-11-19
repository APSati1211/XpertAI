from rest_framework import viewsets
from .models import SiteContent
from .serializers import SiteContentSerializer

class SiteContentViewSet(viewsets.ModelViewSet):
    queryset = SiteContent.objects.all()
    serializer_class = SiteContentSerializer

    def get_queryset(self):
        qs = SiteContent.objects.all()
        page = self.request.query_params.get("page")
        if page:
            qs = qs.filter(page=page)
        return qs
