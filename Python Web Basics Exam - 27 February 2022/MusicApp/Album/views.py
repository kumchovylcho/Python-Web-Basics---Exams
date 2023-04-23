from django.shortcuts import render, redirect

from MusicApp.Album.forms import AlbumForm
from MusicApp.Album.models import BaseAlbum
from MusicApp.Profile.forms import ProfileForm
from MusicApp.Profile.models import BaseProfile


def disable_fields(form):
    for field in form.fields.values():
        field.widget.attrs['disabled'] = 'disabled'


def get_profile(model):
    try:
        profile = model.objects.get()

    except model.DoesNotExist:
        return

    return profile


def index(request):
    context = {
        'profile': get_profile(BaseProfile)
    }

    if context['profile']:
        return home_with_profile(request, 'home-with-profile.html', context)

    return home_with_no_profile(request, 'home-no-profile.html', context)


def home_with_no_profile(request, template, context):

    if request.method == "GET":
        form = ProfileForm()

    else:
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')

    context['form'] = form

    return render(request, template, context)


def home_with_profile(request, template, context):
    context['albums'] = BaseAlbum.objects.all()

    return render(request, template, context)


def add_album(request):
    if request.method == "GET":
        form = AlbumForm()

    else:
        form = AlbumForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form,
        "profile": get_profile(BaseProfile)
    }

    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = BaseAlbum.objects.get(pk=pk)

    context = {
        "album": album,
        "profile": get_profile(BaseProfile)
    }

    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = BaseAlbum.objects.get(pk=pk)

    if request.method == "GET":
        form = AlbumForm(instance=album)

    else:
        form = AlbumForm(request.POST, instance=album)

        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'form': form,
        'album': album,
        'profile': get_profile(BaseProfile)
    }

    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = BaseAlbum.objects.get(pk=pk)
    form = AlbumForm(instance=album)

    if request.method == "GET":
        disable_fields(form)

    else:
        album.delete()
        return redirect('index')

    context = {
        'form': form,
        'profile': get_profile(BaseProfile),
        'album': album
    }

    return render(request, 'delete-album.html', context)
