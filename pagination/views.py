from django.shortcuts import render

from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Product
from .serializers import ProductSerializer
from .pagination import CustomPagination
from .filters import ProductFilter

class ProductListView(ListAPIView):
    queryset = Product.objects.filter(is_available=True).order_by('-created_at')
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['type_of_product', 'description', 'color', 'material']
    ordering_fields = ['price', 'created_at']
