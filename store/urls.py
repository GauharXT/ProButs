from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FavoriteViewSet, CartViewSet

router = DefaultRouter()
router.register(r'favorites', FavoriteViewSet)
router.register(r'cart', CartViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
