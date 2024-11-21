from django.shortcuts import render
from django.http import HttpResponse

import main.views


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')