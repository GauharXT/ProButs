from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    BRAND_CHOICES = [
        ('adidas', 'Adidas'),
        ('demix', 'Demix'),
        ('emporio armani', 'Emporio Armani'),
        ('hugo boss','Hugo Boss'),
        ('jack wolfskin','Jack Wolfskin'),
        ('joss','Joss'),
        ('kelme','Kelme'),
        ('molten','Molten'),
        ('nike','Nike'),
        ('puma','Puma'),
        ('outventure','Outventure'),
        ('speedo', 'Speedo'),
        ('under armour','Under Armour')
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('unisex', 'Unisex'),
    ]

    brand = models.CharField(max_length=100, choices=BRAND_CHOICES)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.brand)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.brand


class Product(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('unisex', 'Unisex'),
    ]

    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='product_images/')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand}"
