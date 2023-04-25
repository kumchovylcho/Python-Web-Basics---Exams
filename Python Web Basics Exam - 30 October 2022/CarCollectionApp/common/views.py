from django.shortcuts import render

from CarCollectionApp.Profile.models import BaseProfile
from CarCollectionApp.common.functionality import get_profile


def index(request):
    context = {
        'profile': get_profile(BaseProfile)
    }

    return render(request, 'index.html', context)
