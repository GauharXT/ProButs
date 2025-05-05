from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductListViewSet

router = DefaultRouter()
router.register(r'productList', ProductListViewSet, basename='product')

urlpatterns = router.urls
