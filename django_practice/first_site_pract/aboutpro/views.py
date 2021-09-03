from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about_pro(request) :
    return HttpResponse("This is the about us repone")