from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
]
