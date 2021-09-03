from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request) :
    #return HttpResponse("Hello I am abhishek Inside Voew of Initpage")
    return render(request,'initpage/welcome.html')