from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Email обязателен')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Используем email вместо username для аутентификации
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']  # Обязательные поля для создания суперпользователя

    def __str__(self):
        return self.email




#Товары
class Product(models.Model):
    GENDER_CHOICES = [
        ('male', 'Мужской'),
        ('female', 'Женский'),
        ('unisex', 'Унисекс'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=10)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='product_images/')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


#Избранное
class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} ♥ {self.product.name}"


#Корзина
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} 🛒 {self.product.name} x {self.quantity}"
