from django.shortcuts import render
from .models import *


# Create your views here.

def home(request):
    return render(request, 'base_layout.html')


def services(request):
    return render(request, 'services.html')
