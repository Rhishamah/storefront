from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


# Create your views here.

def say_hello(request):
    queryset = Product.objects.filter(title__icontains="coffee")
    queryset = Product.objects.filter(collection__id__range=(1, 2, 3))

    return render(request, "hello.html",{"name":"vincent", "products":list(queryset)})