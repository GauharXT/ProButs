# Generated by Django 5.2 on 2025-05-18 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_detail', '0003_alter_category_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
    ]
