from django.db import models

from django.db import models

CATEGORY_CHOICES = [
    ('clothes', 'Clothes'),
    ('shoes', 'Shoes'),
    ('bags', 'Bags'),
    ('accessories', 'Accessories'),
    ('others', 'Others'),
]

class Product(models.Model):
    type_of_product = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=20, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type_of_product
