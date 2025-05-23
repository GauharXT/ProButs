from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    ProductViewSet,
    FavoriteViewSet,
    CartViewSet,
    OrderViewSet,
    RegisterView,
    UserView,
    home,  # допустим, у тебя есть view для главной страницы
)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'favorites', FavoriteViewSet, basename='favorite')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', home, name='store_home'),                     # главная страница магазина
    path('api/', include(router.urls)),                    # все DRF endpoints по /api/...
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/user/', UserView.as_view(), name='user_info'),
]