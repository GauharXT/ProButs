from rest_framework import viewsets, permissions, generics
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters
from .models import Product, Favorite, Cart, CustomUser
from .serializers import (
    ProductSerializer,
    FavoriteSerializer,
    CartSerializer,
    UserSerializer,
    RegisterSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken

# ====== Продукты (Товары) ======
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]  # Доступ для всех


# ====== Регистрация нового пользователя ======
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  # Доступ для всех


# ====== Профиль пользователя ======
class UserView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# ====== Избранное ======
class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        favorite_item = self.get_object()
        favorite_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ====== Корзина ======
class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        cart_item = self.get_object()
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ====== Фильтрация для продуктов ======
class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = filters.CharFilter(field_name='category', lookup_expr='icontains')
    gender = filters.CharFilter(field_name='gender', lookup_expr='exact')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'category', 'gender']

# ====== Продукты (Товары) ======
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filterset_class = ProductFilter  # Применяем фильтрацию
