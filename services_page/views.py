from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ServiceHero, ServiceCTA
from cms.models import Service
from .serializers import ServiceHeroSerializer, ServiceCTASerializer
from cms.serializers import ServiceSerializer

class ServicePageDataView(APIView):
    def get(self, request):
        return Response({
            "hero": ServiceHeroSerializer(ServiceHero.objects.first()).data if ServiceHero.objects.exists() else None,
            "cta": ServiceCTASerializer(ServiceCTA.objects.first()).data if ServiceCTA.objects.exists() else None,
            # Fetch all services directly from CMS app
            "services_list": ServiceSerializer(Service.objects.all().order_by('order'), many=True).data
        })