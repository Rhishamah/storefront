from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Value, F, Func
from django.db.models.functions import Concat
from store.models import Product, Customer


# Create your views here.

def say_hello(request):
    queryset = Customer.objects.annotate(
        full_name=Func(F("first_name"), Value(" "), F("last_name"), function="CONCAT")
    )

#shortcut instead of using the first method 
def say_hello(request):
    queryset = Customer.objects.annotate(
    full_name = Concat("first_name", Value(" "), "last_name"))
    


    return render(request, "hello.html",{"name":"vincent", "result":list(queryset)})