from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'brand', 'category', 'price', 'size',
        'color', 'gender', 'is_available', 'created_at'
    )
    search_fields = ('name', 'brand', 'category', 'color')
    list_filter = ('brand', 'category', 'size', 'color', 'gender', 'is_available', 'created_at')
    ordering = ['-created_at']  # Сортировка по времени создания
    list_display_links = ('name',)  # Сделать название продукта кликабельным
