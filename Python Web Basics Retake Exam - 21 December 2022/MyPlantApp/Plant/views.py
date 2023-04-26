from django.shortcuts import render, redirect

from MyPlantApp.Plant.forms import BasePlantForm
from MyPlantApp.Profile.functionality import get_profile, disable_fields
from MyPlantApp.Plant.models import BasePlant
from MyPlantApp.Profile.models import BaseProfile


def show_catalogue(request):
    context = {
        'profile': get_profile(BaseProfile),
        'plants': BasePlant.objects.all(),
    }

    return render(request, 'catalogue.html', context)


def create_plant(request):
    if request.method == "GET":
        form = BasePlantForm()

    else:
        form = BasePlantForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('show_catalogue')

    context = {
        'profile': get_profile(BaseProfile),
        'form': form
    }

    return render(request, 'create-plant.html', context)


def plant_details(request, pk):
    plant = BasePlant.objects.get(pk=pk)

    context = {
        'profile': get_profile(BaseProfile),
        'plant': plant
    }

    return render(request, 'plant-details.html', context)


def edit_plant(request, pk):
    plant = BasePlant.objects.get(pk=pk)

    if request.method == "GET":
        form = BasePlantForm(instance=plant)

    else:
        form = BasePlantForm(request.POST, instance=plant)

        if form.is_valid():
            form.save()

            return redirect('show_catalogue')

    context = {
        'profile': get_profile(BaseProfile),
        'form': form,
        'plant': plant,
    }

    return render(request, 'edit-plant.html', context)


def delete_plant(request, pk):
    plant = BasePlant.objects.get(pk=pk)
    form = BasePlantForm(instance=plant)

    disable_fields(form)

    if request.method == "POST":
        plant.delete()
        return redirect('show_catalogue')

    context = {
        'profile': get_profile(BaseProfile),
        'form': form,
        'plant': plant,
    }

    return render(request, 'delete-plant.html', context)
