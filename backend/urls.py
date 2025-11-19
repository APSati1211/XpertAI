# C:\Users\Ankur Sati\OneDrive\Desktop\XpertAI_Website\backend\urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line includes all the URLs defined in cms/urls.py under the 'api/' prefix
    path('api/', include('cms.urls')),
]

# This is good practice for serving user-uploaded media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
