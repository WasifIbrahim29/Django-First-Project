from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'first_app/index.html')

def challenge(request):
    return HttpResponse("<h2>My First Challenge<h2>")

def home(request):
    return HttpResponse("<em>Hello world, you're at home route.</em>")

def dashboard(request):
    dashboard_dict= {'dashboard_insert': 'Hello, this is the Dashboard page.'}
    return render(request,'first_app/dashboard.html',context=dashboard_dict)