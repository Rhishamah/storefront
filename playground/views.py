from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Value, F, Func, ExpressionWrapper
from django.db.models.functions import Concat
from store.models import Product, Customer


# Create your views here.

def say_hello(request):
    discounted_price = ExpressionWrapper(F("unit_price") * 0.8, output_field=DecimalField())
    queryset = Customer.objects.annotate(
        discounted_price=discounted_price
    )

    


    return render(request, "hello.html",{"name":"vincent", "result":list(queryset)})