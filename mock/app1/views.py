from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>Welcome to index page of app1</h1>")

def render_method(request):
    return render(request, "sample.html")    
