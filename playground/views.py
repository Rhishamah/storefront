from django.shortcuts import render
from django.http import HttpResponse
from store.models import Order, OrderItem, Product, Customer, Collection

# Create your views here.

def say_hello(request):
    collection = Collection(pk=10)
    collection.delete()
    # or for multiple objects
    Collection.objects.filter(id__gt=5).delete()

    return render(request, "hello.html",{"name":"vincent"})