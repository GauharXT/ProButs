from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Cart, CartItem
from product_detail.models import Product

def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    total_price = sum(item.total_price for item in cart_items)

    return JsonResponse({
        'cart_items': [
            {
                'product': item.product.type_of_product,
                'quantity': item.quantity,
                'total_price': item.total_price
            } for item in cart_items
        ],
        'total_price': total_price
    })

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return JsonResponse({'message': f'{product.type_of_product} added to cart'})

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return JsonResponse({'message': 'Item removed from cart'})
