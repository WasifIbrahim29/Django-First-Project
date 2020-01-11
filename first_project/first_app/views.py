from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def challenge(request):
    return HttpResponse("<h2>My First Challenge<h2>")

def home(request):
    return HttpResponse("<em>Hello world, you're at home route.</em>")

def help(request):
    help_dict= {'help_insert': 'Hello, this is the Help page.'}
    return render(request,'first_app/help.html',context=help_dict)