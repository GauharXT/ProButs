from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.type_of_product', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'type_of_product', 'price', 'category', 'category_name', 'created_at']
