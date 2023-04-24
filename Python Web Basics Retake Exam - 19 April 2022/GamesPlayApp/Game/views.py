from django.shortcuts import render, redirect

from GamesPlayApp.Game.forms import BaseGameForm
from GamesPlayApp.Game.models import BaseGame
from GamesPlayApp.Profile.models import BaseProfile
from GamesPlayApp.Profile.views import get_profile


def disable_fields(form):
    for field in form.fields.values():
        field.widget.attrs['disabled'] = 'disabled'


def create_game(request):
    if request.method == "GET":
        form = BaseGameForm()

    else:
        form = BaseGameForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'form': form,
        'profile': get_profile(BaseProfile)
    }

    return render(request, 'create-game.html', context)


def game_details(request, pk):
    context = {
        'game': BaseGame.objects.get(pk=pk),
        'profile': get_profile(BaseProfile)
    }

    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    game = BaseGame.objects.get(pk=pk)

    if request.method == "GET":
        form = BaseGameForm(instance=game)

    else:
        form = BaseGameForm(request.POST, instance=game)

        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'game': game,
        'profile': get_profile(BaseProfile),
        'form': form,
    }

    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    game = BaseGame.objects.get(pk=pk)

    if request.method == "GET":
        form = BaseGameForm(instance=game)
        disable_fields(form)

    else:
        game.delete()

        return redirect('dashboard')

    context = {
        'game': game,
        'profile': get_profile(BaseProfile),
        'form': form,
    }

    return render(request, 'delete-game.html', context)
