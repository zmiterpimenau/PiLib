from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    result = 2 + 2
    return HttpResponse(f"Hello World!!!{result}")
