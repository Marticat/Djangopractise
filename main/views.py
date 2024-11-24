from django.shortcuts import render
from django.http import HttpResponse

import main.views


def index(request):
    data = {
        'title': 'Main Page',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
