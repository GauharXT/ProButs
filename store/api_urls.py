from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# Зарегистрируйте ваши ViewSet
# Например:
# router.register(r'products', views.ProductViewSet)
# router.register(r'favorites', views.FavoriteViewSet)
# router.register(r'cart', views.CartViewSet)
# router.register(r'orders', views.OrderViewSet)

urlpatterns = router.urls