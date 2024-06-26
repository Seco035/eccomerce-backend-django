# Generated by Django 4.2.11 on 2024-04-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_old_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('M', 'Erkek'), ('F', 'Kadın')], default=1, max_length=1, verbose_name='Cinsiyet'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_home',
            field=models.BooleanField(default=True),
        ),
    ]
