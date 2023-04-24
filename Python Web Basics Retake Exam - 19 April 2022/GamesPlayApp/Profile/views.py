from django.shortcuts import render, redirect

from GamesPlayApp.Game.models import BaseGame
from GamesPlayApp.Profile.forms import CreateProfileForm, BaseProfileForm
from GamesPlayApp.Profile.models import BaseProfile


def get_profile(model):
    try:
        profile = model.objects.get()

    except model.DoesNotExist as ex:
        return

    return profile


def create_profile(request):
    if request.method == "GET":
        form = CreateProfileForm()

    else:
        form = CreateProfileForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def profile_details(request):
    profile = get_profile(BaseProfile)
    games = BaseGame.objects.all()

    name = " ".join(x for x in (profile.first_name, profile.last_name) if x)

    average_rating = sum(x.rating for x in games) / len(games) if games else 0.0

    context = {
        'profile': profile,
        'name': name,
        "games_owned": len(games),
        "average_rating": average_rating
    }

    return render(request, 'details-profile.html', context)


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
        'form': form
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile(BaseProfile)

    if request.method == "POST":
        profile.delete()
        BaseGame.objects.all().delete()

        return redirect('index')

    context = {
        'profile': profile,
    }

    return render(request, 'delete-profile.html', context)
