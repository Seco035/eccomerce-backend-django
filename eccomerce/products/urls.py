from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('products/', products, name="products"),
    path('women/', women_products, name="women_products"),
    path('product/<slug:slug>', product_details, name="product_details"),
    path('cart/', cart, name="cart"),
]
