from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product


# Create your views here.

def say_hello(request):
    # e.g  products: inventory = price to compare two fields 
    queryset = Product.objects.filter(inventory=F("collection__id"))

    return render(request, "hello.html",{"name":"vincent", "products":list(queryset)})