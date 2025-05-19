import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='iexact')
    brand = django_filters.CharFilter(field_name='brand', lookup_expr='iexact')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    size = django_filters.CharFilter(field_name='size', lookup_expr='iexact')
    color = django_filters.CharFilter(field_name='color', lookup_expr='iexact')
    gender = django_filters.CharFilter(field_name='gender', lookup_expr='iexact')
    is_available = django_filters.BooleanFilter(field_name='is_available')

    class Meta:
        model = Product
        fields = ['category', 'brand', 'size', 'color', 'gender', 'is_available', 'price_min', 'price_max']