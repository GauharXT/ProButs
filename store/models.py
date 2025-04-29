from django.db import models

class Category(models.Model):
    GENDER_CHOICES = [
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
        ('ander armour','Under Armour')
    ]
    brand = models.CharField(max_length=100, choices=GENDER_CHOICES)
    material = models.CharField(max_length=100, null=True, blank=True,)

    def __str__(self):
        return self.brand
class Product(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('unisex', 'Unisex'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    # GENDER_BRAND = [
    #     ('adidas', 'Adidas'),
    #     ('demix', 'Demix'),
    #     ('emporio armani', 'Emporio Armani'),
    #     ('hugo boss', 'Hugo Boss'),
    #     ('jack wolfskin', 'Jack Wolfskin'),
    #     ('joss', 'Joss'),
    #     ('kelme', 'Kelme'),
    #     ('molten', 'Molten'),
    #     ('nike', 'Nike'),
    #     ('puma', 'Puma'),
    #     ('outventure', 'Outventure'),
    #     ('speedo', 'Speedo'),
    #     ('ander armour', 'Under Armour')
    # ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=10)
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
