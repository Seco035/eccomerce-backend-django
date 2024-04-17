from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('products/', products, name="products"),
    path('product/p', product_details, name="product_details"),
    path('cart/', cart, name="cart"),
]
