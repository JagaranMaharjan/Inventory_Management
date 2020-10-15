from django.shortcuts import render, redirect, get_object_or_404
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


def edit_device(request, pk, model, form_name):
    item = get_object_or_404(model, pk=pk)
    if request.method == "POST":
        form = form_name(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = form_name(instance=item)
        return render(request, 'inventory/edit_item.html', {'form': form})


def edit_laptop(request, pk):
    return edit_device(request, pk, Laptop, LaptopForm)


def edit_desktop(request, pk):
    return edit_device(request, pk, Desktop, DesktopForm)


def edit_mobile(request, pk):
    return edit_device(request, pk, Mobile, MobileForm)


def delete_laptop(request, pk):
    Laptop.objects.filter(id=pk).delete()
    items = models.Laptop.objects.all()
    context = {
        'items': items,
        'header': "Laptops"
    }
    return render(request, 'inventory/index.html', context)


def delete_desktop(request, pk):
    Desktop.objects.filter(id=pk).delete()
    items = models.Desktop.objects.all()
    context = {
        'items': items,
        'header': "Desktops"
    }
    return render(request, 'inventory/index.html', context)


def delete_mobile(request, pk):
    Mobile.objects.filter(id=pk).delete()
    items = models.Mobile.objects.all()
    context = {
        'items': items,
        'header': "Mobiles"
    }
    return render(request, 'inventory/index.html', context)
