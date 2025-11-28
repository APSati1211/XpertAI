from django.contrib import admin
from .models import LegalPage

@admin.register(LegalPage)
class LegalPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'last_updated')
    search_fields = ('title', 'content')
    # Slug ko automatic generate nahi kar rahe taaki tum manually 'terms' ya 'privacy' set kar sako