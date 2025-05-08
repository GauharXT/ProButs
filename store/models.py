from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

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
        ('male', 'Мужской'),
        ('female', 'Женский'),
        ('kids', 'Детский'),
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
<<<<<<< HEAD
    brand = models.CharField(max_length=100)  # Можно заменить на ForeignKey позже
    category = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
=======
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=100, null=True, blank=True)
>>>>>>> origin/dan
    image = models.ImageField(upload_to='product_images/')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} ♥ {self.product.name}"


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} 🛒 {self.product.name} x {self.quantity}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В обработке'),
        ('completed', 'Завершен'),
        ('cancelled', 'Отменен'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ #{self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"
