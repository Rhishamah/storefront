from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


# Create your views here.

def say_hello(request):
    # select_related is used when the other end of the relationship has only one instance (1)
    # prefetch_related is used when the  other end of the relationship has many objects (n)
    queryset =  Product.objects.prefetch_related("promotions").all()


    return render(request, "hello.html",{"name":"vincent", "products": list(queryset)})