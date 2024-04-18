from django.shortcuts import render, get_object_or_404
from .views import *
from .models import *
# Create your views here.

def index(request):
    
    products = Product.objects.filter(is_home=True)

    return render(request, "index.html", {
        "products":products
    })

def products(request):
    product = Product.objects.filter(is_active=True)
    return render(request, "products.html", {
        "product": product
    })

def cart(request):
    return render(request, "cart.html")

def women_products(request):
    product = Product.objects.filter(gender="F")

    return render(request, "products.html", {
        "product":product

    })

def product_details(request, slug):
    product = Product.objects.get(slug=slug)
    products = Product.objects.filter(is_active=True)

    return render(request, "product_details.html", {
        "product": product,
        "products":products

    })