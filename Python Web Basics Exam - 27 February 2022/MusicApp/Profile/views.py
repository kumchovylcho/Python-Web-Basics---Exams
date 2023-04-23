from django.shortcuts import render, redirect

from MusicApp.Album.models import BaseAlbum
from MusicApp.Album.views import get_profile
from MusicApp.Profile.models import BaseProfile


def profile_details(request):
    albums = BaseAlbum.objects.all()

    context = {
        "albums_qty": len(albums),
        "profile": get_profile(BaseProfile)
    }

    return render(request, "profile-details.html", context)


def delete_profile(request):
    if request.method == "GET":
        return render(request, "profile-delete.html")

    else:
        BaseProfile.objects.get().delete()
        BaseAlbum.objects.all().delete()

    return redirect('index')
