from django.shortcuts import (render,
                              redirect,
                              )

from web_basics.Fruit.models import Fruit
from web_basics.Profile.forms import (CreateProfile,
                                      EditProfile,
                                      DeleteProfile,
                                      )
from web_basics.Profile.functionality import get_profile


def create_profile(request):
    form = CreateProfile()

    if request.method == 'POST':
        form = CreateProfile(request.POST)

        if form.is_valid():
            form.save()

            return redirect("dashboard")

    context = {
        "profile": get_profile(),
        "form": form,
    }

    return render(request, "create-profile.html", context)


def profile_details(request):
    context = {
        "profile": get_profile(),
        "total_posts": Fruit.objects.all().count(),
    }

    return render(request, "details-profile.html", context)


def edit_profile(request):
    profile = get_profile()
    form = EditProfile(instance=profile)

    if request.method == "POST":
        form = EditProfile(request.POST, instance=profile)

        if form.is_valid():
            form.save()

            return redirect("profile_details")

    context = {
        "profile": profile,
        "form": form,
    }

    return render(request, "edit-profile.html", context)


def delete_profile(request):
    profile = get_profile()

    if request.method == "POST":
        form = DeleteProfile(request.POST, instance=profile)
        form.save()

        return redirect("index")

    context = {
        "profile": profile,
    }

    return render(request, "delete-profile.html", context)