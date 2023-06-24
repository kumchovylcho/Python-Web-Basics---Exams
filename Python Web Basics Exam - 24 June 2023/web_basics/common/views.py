from django.shortcuts import render

from web_basics.Fruit.models import Fruit
from web_basics.Profile.functionality import get_profile


def index(request):
    context = {
        "profile": get_profile()
    }

    return render(request, "index.html", context)


def dashboard(request):
    context = {
        "profile": get_profile(),
        "fruits": Fruit.objects.all(),
    }

    return render(request, "dashboard.html", context)

