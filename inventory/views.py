from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
from . import models
from .forms import LaptopForm


def index(request):
    return render(request, 'inventory/index.html')


def display_laptop(request):
    items = models.Laptop.objects.all()
    context = {
        'items': items,
        'header': "Laptops"
    }
    return render(request, 'inventory/index.html', context)


def display_desktop(request):
    items = models.Desktop.objects.all()
    context = {
        'items': items,
        'header': "Desktops"
    }
    return render(request, 'inventory/index.html', context)


def display_mobile(request):
    items = models.Mobile.objects.all()
    context = {
        'items': items,
        'header': "Mobiles"
    }
    return render(request, 'inventory/index.html', context)


def add_device(request, cls):
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = cls()
        return render(request, 'inventory/add_new.html', {'form': form})


def add_laptop(request):
    return add_device(request, LaptopForm)


def add_desktop(request):
    return add_device(request, DesktopForm)


def add_mobile(request):
    return add_device(request, MobileForm)
