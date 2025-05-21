from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    BRAND_CHOICES = [
        ('adidas', 'Adidas'),
        ('demix', 'Demix'),
        ('emporio armani', 'Emporio Armani'),
        ('hugo boss', 'Hugo Boss'),
        ('jack wolfskin', 'Jack Wolfskin'),
        ('joss', 'Joss'),
        ('kelme', 'Kelme'),
        ('molten', 'Molten'),
        ('nike', 'Nike'),
        ('puma', 'Puma'),
        ('outventure', 'Outventure'),
        ('speedo', 'Speedo'),
        ('under armour', 'Under Armour'),
    ]

    brand = models.CharField(max_length=100, choices=BRAND_CHOICES)
    material = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.brand


class Product(models.Model):
    GENDER_CHOICES = [
        ('male', 'Мужской'),
        ('female', 'Женский'),
        ('kids', 'Детский'),
    ]

    SIZE_CHOICES = [
        ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'),
        ('XXL', 'XXL'), ('XXXL', 'XXXL'), ('2XS', '2XS'), ('2XL', '2XL'),
        ('LXL', 'LXL'), ('SM', 'SM'), ('ML', 'ML'),
        ('128', '128'), ('140', '140'), ('152', '152'), ('164', '164'),
        ('30', '30'), ('32', '32'), ('34', '34'), ('34 - 38', '34 - 38'),
        ('35.5', '35.5'), ('36', '36'), ('36.5', '36.5'), ('37', '37'),
        ('37.5', '37.5'), ('38', '38'), ('38.5', '38.5'), ('39', '39'),
        ('40', '40'), ('40.5', '40.5'), ('41', '41'), ('42', '42'),
        ('42.5', '42.5'), ('43', '43'), ('44', '44'), ('44.5', '44.5'),
        ('45', '45'), ('45.5', '45.5'), ('46', '46'), ('46.5', '46.5'),
        ('47', '47'), ('47.5', '47.5'), ('48', '48'), ('48.5', '48.5'),
        ('50', '50'), ('52', '52'), ('54', '54'), ('56', '56'),
        ('58', '58'), ('62', '62'), ('66', '66'), ('ADULT', 'ADULT'),
        ('One', 'One Size'), ('38 - 42', '38 - 42'), ('39 - 42', '39 - 42'),
        ('41 - 43', '41 - 43'), ('42 - 46', '42 - 46'), ('43 - 46', '43 - 46'),
        ('44 - 45.5', '44 - 45.5'), ('46 - 48', '46 - 48'), ('46 - 50', '46 - 50'),
    ]

    COLOR_CHOICES = [
        ('бирюзовый', 'Бирюзовый'), ('бордовый', 'Бордовый'),
        ('голубой', 'Голубой'), ('желто-зеленый', 'Желто-зеленый'),
        ('желтый', 'Желтый'), ('зеленый', 'Зеленый'),
        ('коричневый', 'Коричневый'), ('красный', 'Красный'),
        ('оливковый', 'Оливковый'), ('персиковый', 'Персиковый'),
        ('розовый', 'Розовый'), ('светло-серый', 'Светло-серый'),
        ('светло-синий', 'Светло-синий'), ('серый', 'Серый'),
        ('синий', 'Синий'), ('сиреневый', 'Сиреневый'),
        ('фиолетовый', 'Фиолетовый'), ('черный', 'Черный'),
    ]

    MATERIAL_CHOICES = [
        ('cotton', 'Пахта'), ('wool', 'Жүн'), ('silk', 'Жибек'),
        ('linen', 'Лён'), ('bamboo', 'Бамбук'), ('polyester', 'Полиэстер'),
        ('nylon', 'Нейлон'), ('acrylic', 'Акрил'), ('spandex', 'Эластан'),
        ('microfiber', 'Микрофибра'), ('cotton_polyester', 'Пахта + Полиэстер'),
        ('wool_acrylic', 'Жүн + Акрил'), ('silk_nylon', 'Жибек + Нейлон'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    material = models.CharField(max_length=100, choices=MATERIAL_CHOICES, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='product_images/')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user} ♥ {self.product.name}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user} 🛒 {self.product.name} x{self.quantity}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В обработке'),
        ('completed', 'Завершен'),
        ('cancelled', 'Отменен'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ #{self.id} - {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"
