from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.
from . import models


def index(request):
    items = models.Desktop.objects.all()
    return render(request, 'inventory/index.html', {"items": items})


def display_laptop(request):
    items = models.Laptop.objects.all()
    return render(request, 'inventory/index.html', {"items": items})


def display_desktop(request):
    items = models.Desktop.objects.all()
    return render(request, 'inventory/index.html', {"items": items})


def display_mobile(request):
    items = models.Mobile.objects.all()
    return render(request, 'inventory/index.html', {"items": items})
