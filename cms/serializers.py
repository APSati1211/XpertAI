# cms/serializers.py

from rest_framework import serializers
from .models import SiteContent

class SiteContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteContent
        fields = ['id', 'page', 'section', 'title', 'content', 'image', 'updated_at']
