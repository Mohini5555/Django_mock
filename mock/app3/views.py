from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>Welcome to index page of app2</h1>")

def add(request,num1,num2):
    try:
        num1=int(num1)
    except:
        num1=float(num1)
    try:
        num2=int(num2)
    except:
        num2=float(num2)   

    return HttpResponse(num1 + num2)  

def display(request, data):
    return HttpResponse(f'My name is {data}')        

