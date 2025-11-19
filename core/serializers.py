from rest_framework import serializers
from .models import PageContent

class PageContentSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = PageContent
        fields = ["id", "page", "section", "title", "content", "image", "updated_at"]
