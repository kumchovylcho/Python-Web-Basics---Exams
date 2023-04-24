from django.shortcuts import render

from GamesPlayApp.Game.models import BaseGame
from GamesPlayApp.Profile.models import BaseProfile
from GamesPlayApp.Profile.views import get_profile


def index(request):
    context = {
        'profile': get_profile(BaseProfile)
    }

    return render(request, 'home-page.html', context)


def dashboard(request):
    context = {
        'profile': get_profile(BaseProfile),
        'games': BaseGame.objects.all(),
    }

    return render(request, 'dashboard.html', context)
