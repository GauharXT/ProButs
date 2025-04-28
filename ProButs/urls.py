from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import UserListView, UserDetailView
# Настроим схему для Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Shoes Store API",
        default_version='v1',
        description="Документация для API магазина обуви",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@shoestore.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),  # твоё приложение с API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('api/', include('register.urls')),

]
