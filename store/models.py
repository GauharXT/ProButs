from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Менеджер для кастомного пользователя
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Создает и возвращает обычного пользователя с email и паролем.
        """
        if not email:
            raise ValueError('Пользователи должны иметь email')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Создает и возвращает суперпользователя с email и паролем.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

# Абстрактная модель пользователя
class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Дополнительные поля
    last_login = models.DateTimeField(auto_now=True)

    # Менеджер для пользователя
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'

# Модель для продукта (обуви)
class Product(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('unisex', 'Unisex'),
    ]

    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('bags', 'Bags'),
        ('accessories', 'Accessories'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=5, decimal_places=2)  # Для точности размера
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)  # Выбор категории
    color = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='product_images/')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth import get_user_model
from .models import Product

class Favorite(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # Связь с пользователем
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Связь с продуктом
    quantity = models.PositiveIntegerField(default=1)  # Количество товара в корзине

    def __str__(self):
        return f"{self.user.username} - {self.product.name} (x{self.quantity})"
