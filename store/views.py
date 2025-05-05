from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


from .models import Product

def get_filtered_products(min_price=290, max_price=50990):
    return Product.objects.filter(price__gte=max_price, price__lte=max_price)
