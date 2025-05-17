from django.urls import path
from .views import home, FilteredProductView, CheckoutView

urlpatterns = [
    path('', home, name='home'),  # Главная страница с товарами
    path('api/products/', FilteredProductView.as_view(), name='product-filter'),
    path('api/checkout/', CheckoutView.as_view(), name='checkout'),
]