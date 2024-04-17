from django.shortcuts import render, get_object_or_404
from .views import *
from .models import *
# Create your views here.

def index(request):
    return render(request, "index.html")

def products(request):
    return render(request, "products.html")

def cart(request):
    return render(request, "cart.html")

def product_details(request, slug):
    product = Product.objects.filter(is_home=True)

    return render(request, "product_details.html", {
        "product": product
    })