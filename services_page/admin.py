from django.contrib import admin
from .models import ServiceHero, ServiceCTA

@admin.register(ServiceHero)
class ServiceHeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    def has_add_permission(self, request):
        return ServiceHero.objects.count() == 0

@admin.register(ServiceCTA)
class ServiceCTAAdmin(admin.ModelAdmin):
    list_display = ('title', 'button_text')
    def has_add_permission(self, request):
        return ServiceCTA.objects.count() == 0