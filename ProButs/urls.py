from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('store.urls')),  # Store тиркемеси учун URL
    path('admin/', admin.site.urls),  # Админ панелинин URL'и  ✅
    path('users/', include('users.urls')),  # Users тиркемеси учун URL
    path('api/', include('productList.urls')),  # ProductList API учун URL  ✅
    path('pro/', include('product_detail.urls')),  # ProductDetail URL
    path('cart/', include('cart.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
