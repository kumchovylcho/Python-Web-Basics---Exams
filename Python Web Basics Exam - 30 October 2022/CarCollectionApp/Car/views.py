from django.shortcuts import render, redirect

from CarCollectionApp.Car.forms import BaseCarForm
from CarCollectionApp.Car.models import BaseCar
from CarCollectionApp.Profile.models import BaseProfile
from CarCollectionApp.common.functionality import get_profile, disable_fields


def show_catalogue(request):
    all_cars = BaseCar.objects.all()

    context = {
        'profile': get_profile(BaseProfile),
        'cars': all_cars,
        'all_cars': len(all_cars),
    }

    return render(request, 'catalogue.html', context)


def create_car(request):
    if request.method == "GET":
        form = BaseCarForm()

    else:
        form = BaseCarForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('show_catalogue')

    context = {
        'profile': get_profile(BaseProfile),
        'form': form
    }

    return render(request, 'car-create.html', context)


def car_details(request, pk):
    car = BaseCar.objects.get(pk=pk)

    context = {
        'profile': get_profile(BaseProfile),
        'car': car,
    }

    return render(request, 'car-details.html', context)


def edit_car(request, pk):
    car = BaseCar.objects.get(pk=pk)

    if request.method == "GET":
        form = BaseCarForm(instance=car)

    else:
        form = BaseCarForm(request.POST, instance=car)

        if form.is_valid():
            form.save()

            return redirect('show_catalogue')

    context = {
        'profile': get_profile(BaseProfile),
        'form': form,
        'car': car,
    }

    return render(request, 'car-edit.html', context)


def delete_car(request, pk):
    car = BaseCar.objects.get(pk=pk)
    form = BaseCarForm(instance=car)

    disable_fields(form)

    if request.method == "POST":
        car.delete()

        return redirect('show_catalogue')

    context = {
        'profile': get_profile(BaseProfile),
        'form': form,
        'car': car,
    }

    return render(request, 'car-delete.html', context)
