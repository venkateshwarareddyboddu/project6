from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def kohli(request):
    return HttpResponse('<h1> is the best chasing master<h1/>')

