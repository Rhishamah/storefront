from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product


# Create your views here.

def say_hello(request):
    # sorting data 
    product = Product.objects.filter(collection__id=1).order_by("unit_price")[0]
    product = Product.objects.earliest("unit_price")
    return render(request, "hello.html",{"name":"vincent", "product":product})