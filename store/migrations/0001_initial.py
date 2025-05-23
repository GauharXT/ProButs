# Generated by Django 5.2.1 on 2025-05-09 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_product', models.CharField(choices=[('barsyetka', 'Барсетка'), ('bolero', 'Болеро'), ('vetrovka', 'Ветровка'), ('zhiletka', 'Жилетка'), ('kepka', 'Кепка'), ('kovrik_dlya_yogi', 'Коврик для йоги'), ('kostyum', 'Костюм'), ('krossovki', 'Кроссовки'), ('kurtka', 'Куртка'), ('losiny', 'Лосины'), ('mayka', 'Майка'), ('nakolennik', 'Наколенник'), ('napulsnik', 'Напульсник'), ('noski', 'Носки'), ('ochki', 'Очки'), ('perchatki', 'Перчатки'), ('perchatki_dlya_treninga', 'Перчатки для тренинга'), ('platye', 'Платье'), ('polo', 'Поло'), ('ryukzak', 'Рюкзак'), ('sandalii', 'Сандалии'), ('slantsy', 'Сланцы'), ('sumka', 'Сумка'), ('sumka_na_poyas', 'Сумка на пояс'), ('tolstovka', 'Толстовка'), ('top', 'Топ'), ('trusy', 'Трусы'), ('futbolka_base', 'Футболка BASE'), ('futbolka_dl_rukav', 'Футболка дл рукав'), ('futbolka', 'Футболка.'), ('shapka', 'Шапка'), ('shorty', 'Шорты'), ('shorty_base', 'Шорты BASE'), ('shtany', 'Штаны'), ('shtany_base', 'Штаны BASE')], max_length=100, null=True)),
                ('brand', models.CharField(choices=[('adidas', 'Adidas'), ('demix', 'Demix'), ('emporio armani', 'Emporio Armani'), ('hugo boss', 'Hugo Boss'), ('jack wolfskin', 'Jack Wolfskin'), ('joss', 'Joss'), ('kelme', 'Kelme'), ('molten', 'Molten'), ('nike', 'Nike'), ('puma', 'Puma'), ('outventure', 'Outventure'), ('speedo', 'Speedo'), ('under armour', 'Under Armour')], max_length=100)),
                ('material', models.CharField(blank=True, choices=[('cotton', 'Пахта'), ('wool', 'Жүн'), ('silk', 'Жибек'), ('linen', 'Лён'), ('bamboo', 'Бамбук'), ('polyester', 'Полиэстер'), ('nylon', 'Нейлон'), ('acrylic', 'Акрил'), ('spandex', 'Эластан'), ('microfiber', 'Микрофибра'), ('cotton_polyester', 'Пахта + Полиэстер'), ('wool_acrylic', 'Жүн + Акрил'), ('silk_nylon', 'Жибек + Нейлон')], max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category_images/')),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_product', models.CharField(choices=[('barsyetka', 'Барсетка'), ('bolero', 'Болеро'), ('vetrovka', 'Ветровка'), ('zhiletka', 'Жилетка'), ('kepka', 'Кепка'), ('kovrik_dlya_yogi', 'Коврик для йоги'), ('kostyum', 'Костюм'), ('krossovki', 'Кроссовки'), ('kurtka', 'Куртка'), ('losiny', 'Лосины'), ('mayka', 'Майка'), ('nakolennik', 'Наколенник'), ('napulsnik', 'Напульсник'), ('noski', 'Носки'), ('ochki', 'Очки'), ('perchatki', 'Перчатки'), ('perchatki_dlya_treninga', 'Перчатки для тренинга'), ('platye', 'Платье'), ('polo', 'Поло'), ('ryukzak', 'Рюкзак'), ('sandalii', 'Сандалии'), ('slantsy', 'Сланцы'), ('sumka', 'Сумка'), ('sumka_na_poyas', 'Сумка на пояс'), ('tolstovka', 'Толстовка'), ('top', 'Топ'), ('trusy', 'Трусы'), ('futbolka_base', 'Футболка BASE'), ('futbolka_dl_rukav', 'Футболка дл рукав'), ('futbolka', 'Футболка.'), ('shapka', 'Шапка'), ('shorty', 'Шорты'), ('shorty_base', 'Шорты BASE'), ('shtany', 'Штаны'), ('shtany_base', 'Штаны BASE')], max_length=100)),
                ('brand', models.CharField(choices=[('adidas', 'Adidas'), ('demix', 'Demix'), ('emporio armani', 'Emporio Armani'), ('hugo boss', 'Hugo Boss'), ('jack wolfskin', 'Jack Wolfskin'), ('joss', 'Joss'), ('kelme', 'Kelme'), ('molten', 'Molten'), ('nike', 'Nike'), ('puma', 'Puma'), ('outventure', 'Outventure'), ('speedo', 'Speedo'), ('under armour', 'Under Armour')], max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL'), ('2XS', '2XS'), ('2XL', '2XL'), ('LXL', 'LXL'), ('SM', 'SM'), ('ML', 'ML'), ('128', '128'), ('140', '140'), ('152', '152'), ('164', '164'), ('30', '30'), ('32', '32'), ('34', '34'), ('34 - 38', '34 - 38'), ('35.5', '35.5'), ('36', '36'), ('36.5', '36.5'), ('37', '37'), ('37.5', '37.5'), ('38', '38'), ('38.5', '38.5'), ('39', '39'), ('40', '40'), ('40.5', '40.5'), ('41', '41'), ('42', '42'), ('42.5', '42.5'), ('43', '43'), ('44', '44'), ('44.5', '44.5'), ('45', '45'), ('45.5', '45.5'), ('46', '46'), ('46.5', '46.5'), ('47', '47'), ('47.5', '47.5'), ('48', '48'), ('48.5', '48.5'), ('50', '50'), ('52', '52'), ('54', '54'), ('56', '56'), ('58', '58'), ('62', '62'), ('66', '66'), ('ADULT', 'ADULT'), ('One', 'One Size'), ('38 - 42', '38 - 42'), ('39 - 42', '39 - 42'), ('41 - 43', '41 - 43'), ('42 - 46', '42 - 46'), ('43 - 46', '43 - 46'), ('44 - 45.5', '44 - 45.5'), ('46 - 48', '46 - 48'), ('46 - 50', '46 - 50')], max_length=20)),
                ('color', models.CharField(choices=[('бирюзовый', 'Бирюзовый'), ('бордовый', 'Бордовый'), ('голубой', 'Голубой'), ('желто-зеленый', 'Желто-зеленый'), ('желтый', 'Желтый'), ('зеленый', 'Зеленый'), ('коричневый', 'Коричневый'), ('красный', 'Красный'), ('оливковый', 'Оливковый'), ('персиковый', 'Персиковый'), ('розовый', 'Розовый'), ('светло-серый', 'Светло-серый'), ('светло-синий', 'Светло-синий'), ('серый', 'Серый'), ('синий', 'Синий'), ('сиреневый', 'Сиреневый'), ('фиолетовый', 'Фиолетовый'), ('черный', 'Черный')], max_length=50)),
                ('material', models.CharField(blank=True, choices=[('cotton', 'Пахта'), ('wool', 'Жүн'), ('silk', 'Жибек'), ('linen', 'Лён'), ('bamboo', 'Бамбук'), ('polyester', 'Полиэстер'), ('nylon', 'Нейлон'), ('acrylic', 'Акрил'), ('spandex', 'Эластан'), ('microfiber', 'Микрофибра'), ('cotton_polyester', 'Пахта + Полиэстер'), ('wool_acrylic', 'Жүн + Акрил'), ('silk_nylon', 'Жибек + Нейлон')], max_length=100, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('unisex', 'Unisex')], max_length=10)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
    ]
