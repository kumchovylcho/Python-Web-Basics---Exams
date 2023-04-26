from django.shortcuts import render, redirect

from MyPlantApp.Plant.models import BasePlant
from MyPlantApp.Profile.functionality import get_profile
from MyPlantApp.Profile.forms import CreateProfileForm, BaseProfileForm
from MyPlantApp.Profile.models import BaseProfile


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
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def profile_details(request):
    context = {
        'profile': get_profile(BaseProfile),
        'all_plants': len(BasePlant.objects.all())
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

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile(BaseProfile)

    if request.method == "POST":
        profile.delete()
        BasePlant.objects.all().delete()

        return redirect('index')

    context = {
        'profile': profile,
    }

    return render(request, 'delete-profile.html', context)