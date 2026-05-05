from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from store.models import Order, OrderItem, Product, Customer, Collection

# Create your views here.

def say_hello(request):
    with connection.cursor() as cursor:
        cursor.execute()
        # for executing stored procedures 
        cursor.callproc("get_customers", [1,2,3, 'a'])

    return render(request, "hello.html",{"name":"vincent", "result": list(queryset)})