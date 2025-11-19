from django.contrib import admin
from .models import SiteContent

@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ("page", "section", "title", "updated_at")
    list_filter = ("page",)
    search_fields = ("page", "section", "title")
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Use PAGE_CHOICES from the model to define allowed pages
        allowed_pages = [choice[0] for choice in SiteContent.PAGE_CHOICES]
        return qs.filter(page__in=allowed_pages)

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "page":
            # Use PAGE_CHOICES from the model for the dropdown
            kwargs["choices"] = SiteContent.PAGE_CHOICES
        return super().formfield_for_choice_field(db_field, request, **kwargs)
