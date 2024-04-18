from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField("Kategori", max_length=100)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    genders = (
        ('M','Erkek'),
        ('F','Kadın'),
    )
    title = models.CharField("Başlık", max_length=150)
    description = models.TextField("Açıklama")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to="products")
    slug = models.SlugField(unique=True, db_index=True, default="")
    is_active = models.BooleanField(default=True)
    is_home = models.BooleanField(default=True)
    gender = models.CharField("Cinsiyet", max_length=1, choices=genders, default=1)
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} {self.price}"

    