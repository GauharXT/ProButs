from django.contrib import admin
from .models import Product, Order, OrderItem, Cart, Favorite

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'brand', 'category', 'price', 'size',
        'color', 'gender', 'is_available', 'created_at'
    )
    search_fields = ('name', 'brand', 'category', 'color')
    list_filter = ('brand', 'category', 'size', 'color', 'gender', 'is_available', 'created_at')
    ordering = ['-created_at']
    list_display_links = ('name',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username',)
    inlines = [OrderItemInline]
    readonly_fields = ('total_price',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'is_active')
    search_fields = ('user__username', 'product__name')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    search_fields = ('user__username', 'product__name')
