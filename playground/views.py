from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from store.models import Order, OrderItem, Product, Customer, Collection

# Create your views here.

def say_hello(request):


    return render(request, "hello.html",{"name":"vincent"})