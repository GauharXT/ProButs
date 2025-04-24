from rest_framework import serializers
from .models import Product, CustomUser

# Сериализатор для продукта
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Сериализуем все поля модели Product

# Сериализатор для пользователя
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
from rest_framework import serializers
from .models import Favorite, Cart, Product

# Сериализатор для избранного
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'product']

# Сериализатор для корзины
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user', 'product', 'quantity']

# Сериализатор для продукта (уже был, не изменился)
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
