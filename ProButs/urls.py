from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your_email@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('store.urls')),  # Store тиркемеси учун URL
    path('admin/', admin.site.urls),  # Админ панелинин URL'и  ✅
    path('users/', include('users.urls')),  # Users тиркемеси учун URL
    path('productList/', include('productList.urls')),  # ProductList API учун URL  ✅
    path('product_detail/', include('product_detail.urls')),  # ProductDetail URL
    path('cart/', include('cart.urls')),
    path('register/', include('register.urls')),
    # Swagger UI үчүн URL'дер:
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
