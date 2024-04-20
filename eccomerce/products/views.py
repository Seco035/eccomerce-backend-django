from django.shortcuts import render, redirect
from .views import *
from .models import *
from .forms import ContactForm
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

def ty(request):
    return render(request, "thankyou.html")

def contact(request):


    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect("ty")
    else:
        contact_form = ContactForm
    
    return render(request, "contact.html", {'contact_form': contact_form})

def men_products(request):
    product = Product.objects.filter(gender="M")

    return render(request, "products.html", {
        "product":product

    })

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