from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from store.models import Order
from store.models import OrderItem


# Create your views here.

def say_hello(request):
    # select_related is used when the other end of the relationship has only one instance (1)
    # prefetch_related is used when the  other end of the relationship has many objects (n)
    queryset =  Order.objects.select_related(
        "customer").prefetch_related("orderitem_set__product").order_by("-placed_at")[:5]


    return render(request, "hello.html",{"name":"vincent", "orders": list(queryset)})