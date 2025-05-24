from django.conf import settings
from django.db import models
from product_detail.models import Product

# Колдонуучунун корзинасын билдирген модел
class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Колдонуучунун модели менен байланыш тузулот
        on_delete=models.CASCADE   # Колдонуучу очурулсо, корзинасы да очот
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Корзина качан тузгонун  автоматтык турдо сактайт

    def __str__(self):
        # Админ панелде жана башка жерлерде "Cart 1 for username" турундо корунот
        return f"Cart {self.id} for {self.user.username}"


# Корзинадагы ар бир товарды билдирген модель
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,                         # Товар кайсы корзинада экенин корсотот
        related_name='items',         # cart.items.all() менен корзинадагы товарларды алабыз
        on_delete=models.CASCADE      # Корзина очурулсо, товарлар да очот
    )
    product = models.ForeignKey(
        Product,                      # Товар кайсы продукт экенин корсотот
        on_delete=models.CASCADE      # Продукт очурулсо, бул жазуу да очот
    )
    quantity = models.PositiveIntegerField(default=1)  # Товардын саны (терс сан болбойт)

    def __str__(self):
        # бул товар бар экенин жана канча даана бар экенин корсотот
        return f"{self.product.type_of_product} x {self.quantity}"

    @property
    def total_price(self):
        # Товардын жалпы баасын эсептейт: баа * сан
        return self.product.price * self.quantity
