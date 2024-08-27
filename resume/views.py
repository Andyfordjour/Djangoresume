from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def api_project(request):
    return render(request, 'api_project.html')

def crm(request):
    return render(request, 'crm.html')

def restaurant(request):
    return render(request, 'restaurant.html')

