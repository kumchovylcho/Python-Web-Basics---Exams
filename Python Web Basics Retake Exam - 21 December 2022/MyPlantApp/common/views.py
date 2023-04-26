from django.shortcuts import render

from MyPlantApp.Profile.functionality import get_profile
from MyPlantApp.Profile.models import BaseProfile


def index(request):
    context = {
        'profile': get_profile(BaseProfile)
    }

    return render(request, 'home-page.html', context)
