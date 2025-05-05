from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'brand', 'material',)
    search_fields = ('brand', 'material',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'brand', 'category', 'price', 'size',
        'color', 'material', 'gender', 'is_available', 'created_at'
    )
    search_fields = ( 'brand', 'color', 'material')
    list_filter = ('brand', 'category', 'size', 'color', 'gender', 'is_available', 'created_at')
