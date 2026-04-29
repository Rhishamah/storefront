from django.shortcuts import render
from django.http import HttpResponse
from store.models import Order, OrderItem, Product, Customer, Collection

# Create your views here.

def say_hello(request):
    # collection = Collection.objects.get(pk=11)
    # collection.featured_product = None
    # collection.save()

    Collection.objects.filter(pk=10).update(featured_product=None)
    return render(request, "hello.html",{"name":"vincent"})