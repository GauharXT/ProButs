from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Category(models.Model):
    GENDER_CHOICES = [
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
        ('under armour', 'Under Armour')
    ]
    CATEGORY_NAMES = [
        ('barsyetka', 'Барсетка'),
        ('bolero', 'Болеро'),
        ('vetrovka', 'Ветровка'),
        ('zhiletka', 'Жилетка'),
        ('kepka', 'Кепка'),
        ('kovrik_dlya_yogi', 'Коврик для йоги'),
        ('kostyum', 'Костюм'),
        ('krossovki', 'Кроссовки'),
        ('kurtka', 'Куртка'),
        ('losiny', 'Лосины'),
        ('mayka', 'Майка'),
        ('nakolennik', 'Наколенник'),
        ('napulsnik', 'Напульсник'),
        ('noski', 'Носки'),
        ('ochki', 'Очки'),
        ('perchatki', 'Перчатки'),
        ('perchatki_dlya_treninga', 'Перчатки для тренинга'),
        ('platye', 'Платье'),
        ('polo', 'Поло'),
        ('ryukzak', 'Рюкзак'),
        ('sandalii', 'Сандалии'),
        ('slantsy', 'Сланцы'),
        ('sumka', 'Сумка'),
        ('sumka_na_poyas', 'Сумка на пояс'),
        ('tolstovka', 'Толстовка'),
        ('top', 'Топ'),
        ('trusy', 'Трусы'),
        ('futbolka_base', 'Футболка BASE'),
        ('futbolka_dl_rukav', 'Футболка дл рукав'),
        ('futbolka', 'Футболка.'),
        ('shapka', 'Шапка'),
        ('shorty', 'Шорты'),
        ('shorty_base', 'Шорты BASE'),
        ('shtany', 'Штаны'),
        ('shtany_base', 'Штаны BASE'),
    ]

    MATERIAL_CHOICES = [
        ('cotton', 'Пахта'),
        ('wool', 'Жүн'),
        ('silk', 'Жибек'),
        ('linen', 'Лён'),
        ('bamboo', 'Бамбук'),
        ('polyester', 'Полиэстер'),
        ('nylon', 'Нейлон'),
        ('acrylic', 'Акрил'),
        ('spandex', 'Эластан'),
        ('microfiber', 'Микрофибра'),
        ('cotton_polyester', 'Пахта + Полиэстер'),
        ('wool_acrylic', 'Жүн + Акрил'),
        ('silk_nylon', 'Жибек + Нейлон'),
    ]

    type_of_product = models.CharField(max_length=100, null=True, choices=CATEGORY_NAMES)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, null=False, default='default_brand', choices=GENDER_CHOICES)
    material = models.CharField(max_length=100, null=True, blank=True, choices=MATERIAL_CHOICES)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)  # Corrected the parenthesis here

class Product(models.Model):
    CATEGORY_NAMES = [
        ('barsyetka', 'Барсетка'),
        ('bolero', 'Болеро'),
        ('vetrovka', 'Ветровка'),
        ('zhiletka', 'Жилетка'),
        ('kepka', 'Кепка'),
        ('kovrik_dlya_yogi', 'Коврик для йоги'),
        ('kostyum', 'Костюм'),
        ('krossovki', 'Кроссовки'),
        ('kurtka', 'Куртка'),
        ('losiny', 'Лосины'),
        ('mayka', 'Майка'),
        ('nakolennik', 'Наколенник'),
        ('napulsnik', 'Напульсник'),
        ('noski', 'Носки'),
        ('ochki', 'Очки'),
        ('perchatki', 'Перчатки'),
        ('perchatki_dlya_treninga', 'Перчатки для тренинга'),
        ('platye', 'Платье'),
        ('polo', 'Поло'),
        ('ryukzak', 'Рюкзак'),
        ('sandalii', 'Сандалии'),
        ('slantsy', 'Сланцы'),
        ('sumka', 'Сумка'),
        ('sumka_na_poyas', 'Сумка на пояс'),
        ('tolstovka', 'Толстовка'),
        ('top', 'Топ'),
        ('trusy', 'Трусы'),
        ('futbolka_base', 'Футболка BASE'),
        ('futbolka_dl_rukav', 'Футболка дл рукав'),
        ('futbolka', 'Футболка.'),
        ('shapka', 'Шапка'),
        ('shorty', 'Шорты'),
        ('shorty_base', 'Шорты BASE'),
        ('shtany', 'Штаны'),
        ('shtany_base', 'Штаны BASE'),
    ]

    name = models.CharField(max_length=255, choices=CATEGORY_NAMES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
