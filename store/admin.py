from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'brand', 'category', 'price', 'size',
        'color', 'material', 'gender', 'is_available', 'created_at'
    )
    search_fields = ('name', 'brand', 'category__name', 'color', 'material')
    list_filter = ('brand', 'category', 'size', 'color', 'gender', 'is_available', 'created_at')
