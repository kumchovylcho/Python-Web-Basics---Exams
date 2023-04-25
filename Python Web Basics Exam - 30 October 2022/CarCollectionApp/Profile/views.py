from django.shortcuts import render, redirect

from CarCollectionApp.Car.models import BaseCar
from CarCollectionApp.Profile.forms import CreateProfileForm, BaseProfileForm
from CarCollectionApp.Profile.models import BaseProfile
from CarCollectionApp.common.functionality import get_profile


def create_profile(request):
    if request.method == "GET":
        form = CreateProfileForm()

    else:
        form = CreateProfileForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('show_catalogue')

    context = {
        'profile': get_profile(BaseProfile),
        'form': form
    }

    return render(request, 'profile-create.html', context)


def profile_details(request):
    profile = get_profile(BaseProfile)
    cars = BaseCar.objects.all()

    profile_name = " ".join(x for x in (profile.first_name, profile.last_name) if x)
    all_cars_price = sum(car.price for car in cars)

    context = {
        'profile': profile,
        'profile_name': profile_name,
        'all_cars_price': all_cars_price,
    }

    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = get_profile(BaseProfile)

    if request.method == "GET":
        form = BaseProfileForm(instance=profile)

    else:
        form = BaseProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()

            return redirect('profile_details')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile(BaseProfile)
    cars = BaseCar.objects.all()

    context = {
        'profile': get_profile(BaseProfile)
    }

    if request.method == "GET":
        return render(request, 'profile-delete.html', context)

    profile.delete()
    cars.delete()

    return redirect('index')
