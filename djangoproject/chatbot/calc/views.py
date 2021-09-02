from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def firstpage(request) :
    return HttpResponse("Hello World")
