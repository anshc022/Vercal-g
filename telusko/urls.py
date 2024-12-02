

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('travello.urls')),  # Include URLs from the 'travello' app
    path('admin/', admin.site.urls),  # Admin site URL
    path('accounts/', include('accounts.urls')),  # Include URLs from the 'accounts' app
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
