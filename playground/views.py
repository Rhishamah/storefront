from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem

# Create your views here.

def say_hello(request):
    


    return render(request, "hello.html",{"name":"vincent"})