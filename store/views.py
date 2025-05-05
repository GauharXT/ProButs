from rest_framework import viewsets, permissions, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Prefetch, Sum, F
from rest_framework import serializers
from .models import Product, Cart, Order, Favorite
from .serializers import (
    ProductSerializer,
    CartSerializer,
    OrderSerializer,
    FavoriteSerializer,
    ProductDetailSerializer
)
from .filters import ProductFilter

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related('brand')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'brand__name']
    ordering_fields = ['price', 'created_at']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductSerializer

    @action(detail=True, methods=['post', 'delete'], permission_classes=[permissions.IsAuthenticated])
    def favorite(self, request, pk=None):
        product = self.get_object()
        if request.method == 'POST':
            favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)
            if not created:
                return Response({'detail': 'Товар уже в избранном'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'status': 'Товар добавлен в избранное'}, status=status.HTTP_201_CREATED)
        Favorite.objects.filter(user=request.user, product=product).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'product_id'

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user).select_related('product')

    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        cart_item, created = Cart.objects.get_or_create(
            user=self.request.user,
            product=product,
            defaults={'quantity': 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related('products')

    def perform_create(self, serializer):
        cart_items = Cart.objects.filter(user=self.request.user)
        if not cart_items.exists():
            raise serializers.ValidationError("Корзина пуста")
        total = sum(item.product.price * item.quantity for item in cart_items)
        order = serializer.save(user=self.request.user, total_price=total)
        order.products.set([item.product for item in cart_items])
        cart_items.delete()

class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user).select_related('product')

    def perform_create(self, serializer):
        if Favorite.objects.filter(user=self.request.user, product=serializer.validated_data['product']).exists():
            raise serializers.ValidationError("Товар уже в избранном")
        serializer.save(user=self.request.user)