from django.urls import path
from .views import home, FilteredProductView, CheckoutView

urlpatterns = [
    path('api/products/', FilteredProductView.as_view()),
    path('api/checkout/', CheckoutView.as_view()),
]