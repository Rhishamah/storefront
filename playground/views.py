from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Value, F
from store.models import Product, Customer


# Create your views here.

def say_hello(request):
    queryset = Customer.objects.annotate(new_id=F("id"))

    return render(request, "hello.html",{"name":"vincent", "result":list(queryset)})