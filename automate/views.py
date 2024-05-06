from django.http import HttpResponse
from django.shortcuts import render
from templates import main

# Create your views here.
def home(request):
    return render(request, main)
