from django.shortcuts import render
from django.http import HttpResponse
from store.models import Order, OrderItem, Product, Customer, Collection

# Create your views here.

def say_hello(request):
    collection = Collection()
    collection.title = "Video Games"
    collection.featured_product = Product(pk=1)
    collection.save()

    return render(request, "hello.html",{"name":"vincent"})