from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil
# Create your views here.



def index(request):
    products=product.objects.all()
    n=len(products)
    slides=n//4 + ceil((n/4)-(n//4))
    params = {"numslide": slides, "range": range(1, slides),"product": products}
    return render(request,"shopping/index.html",params)

def about(request):
    return render(request,"shopping/about.html")

def contact(request):
    return render(request,"shopping/contact.html")

def tracker(request):
    return render(request,"shopping/tracker.html")

def productview(request):
    return render(request,"shopping/productview.html")

def checkout(request):
    return render(request,"shopping/checkout.html")

def search(request):
    return render(request,"shopping/index.html")
