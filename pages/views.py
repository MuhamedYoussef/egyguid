from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import City


def index(request):
    context = {
        'cities': City.objects.order_by('id')
    }
    return render(request, 'pages/index.html', context)

def city(request, slug):
    context = {
        'city': get_object_or_404(City, slug=slug)
    }
    return render(request, 'pages/city.html', context)

def about(request):
    return render(request, 'pages/about.html')
