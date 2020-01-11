from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def challenge(request):
    return HttpResponse("<h2>My First Challenge<h2>")

def home(request):
    return HttpResponse("<em>Hello world, you're at home route.</em>")