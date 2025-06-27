from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.filter(category__name="Featured")
    return render(request, "store/index.html", {"products": products})
