from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte') #	"greater than or equal" (≥)
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')#	"less than or equal" (≤)
    category = filters.CharFilter(field_name="category", lookup_expr='iexact')
    color = filters.CharFilter(field_name="color", lookup_expr='icontains')
    size = filters.CharFilter(field_name="size", lookup_expr='icontains')
    material = filters.CharFilter(field_name="material", lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price', 'color', 'size', 'material']
