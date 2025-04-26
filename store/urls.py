from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, FavoriteViewSet, CartViewSet, RegisterView, UserView

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'favorites', FavoriteViewSet, basename='favorites')
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/user/', UserView.as_view(), name='user-profile'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
