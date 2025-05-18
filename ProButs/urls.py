from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('store.urls')),
    path('home/', include('store.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('api/', include('store.api_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)