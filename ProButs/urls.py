from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('store.urls')),        # Главная страница — все пути магазина
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Пользовательские маршруты
    # path('api/', include('store.api_urls')),  # если нужен API на отдельном URL
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)