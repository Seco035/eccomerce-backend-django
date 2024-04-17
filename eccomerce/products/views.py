from django.shortcuts import render
from .views import *
# Create your views here.

def index(request):
    return render(request, "index.html")

def products(request):
    return render(request, "products.html")

def cart(request):
    return render(request, "cart.html")

def product_details(request):
    return render(request, "product_details.html")