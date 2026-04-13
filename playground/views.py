from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product


# Create your views here.

def say_hello(request):
    # sorting data 
    queryset = Product.objects.all()[:5] 

    return render(request, "hello.html",{"name":"vincent", "products": list(queryset)})