# Generated by Django 4.2.11 on 2024-04-17 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Ürün', 'verbose_name_plural': 'Ürünler'},
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Açıklama'),
        ),
    ]