# Generated by Django 4.2.11 on 2024-04-17 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
