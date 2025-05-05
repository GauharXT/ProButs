from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    ProductViewSet,
    FavoriteViewSet,
    CartViewSet,
    OrderViewSet,
    RegisterView,
    UserView
)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'favorites', FavoriteViewSet, basename='favorite')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),

    # JWT
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Registration
    path('auth/register/', RegisterView.as_view(), name='register'),

    # User info
    path('auth/user/', UserView.as_view(), name='user_info'),
]
