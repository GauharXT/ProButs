from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('type_of_product', 'slug')
    search_fields = ('type_of_product',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'type_of_product', 'brand', 'category', 'price', 'size',
        'color', 'material', 'gender', 'is_available', 'created_at'
    )
    search_fields = ('type_of_product', 'brand', 'category__type_of_product', 'color', 'material')
    list_filter = ('brand', 'category', 'size', 'color', 'gender', 'is_available', 'created_at')
