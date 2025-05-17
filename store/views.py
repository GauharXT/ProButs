from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from .filters import ProductFilter  # Импорт вашего фильтра

# Вью для отображения товаров на главной странице (обычный рендеринг)
def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

# API для получения фильтрованных товаров
class FilteredProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

# API для оформления заказа
class CheckoutView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)