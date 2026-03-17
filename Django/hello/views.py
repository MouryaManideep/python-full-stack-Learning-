from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello")

def mourya(request):
    return HttpResponse("Hello Mourya")

def greet(request, name):
    return HttpResponse(f"Heloo  {name}! - greet")