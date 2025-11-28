from rest_framework import serializers
from .models import ServiceHero, ServiceCTA
from cms.models import Service # Import existing Service model from CMS
from cms.serializers import ServiceSerializer # Re-use existing serializer

class ServiceHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceHero
        fields = '__all__'

class ServiceCTASerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCTA
        fields = '__all__'