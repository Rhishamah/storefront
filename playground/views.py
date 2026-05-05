from django.shortcuts import render
from django.db import transaction
from django.http import HttpResponse
from store.models import Order, OrderItem, Product, Customer, Collection

# Create your views here.

def say_hello(request):
    queryset = Product.objects.raw("SELECT id, title FROM store_product")


    return render(request, "hello.html",{"name":"vincent", "result": list(queryset)})