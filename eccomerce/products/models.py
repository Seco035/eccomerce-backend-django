from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Movie(models.Model):
    title = models.CharField("Başlık", max_length=150)
    description = RichTextField("Açıklama")
    image = models.ImageField(upload_to="products")
    slug = models.SlugField(unique=True, db_index=True)
    is_active = models.BooleanField()
    is_home = models.BooleanField()

    def __str__(self):
        return self.title