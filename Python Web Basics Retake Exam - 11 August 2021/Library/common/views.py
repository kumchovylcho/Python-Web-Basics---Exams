from django.shortcuts import render, redirect

from Library.Book.models import BaseBook
from Library.Profile.forms import ProfileForm
from Library.Profile.models import BaseProfile


def get_profile():
    try:
        profile = BaseProfile.objects.get()

    except BaseProfile.DoesNotExist:
        return

    return profile


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    if profile:
        context.update({
            'books': BaseBook.objects.all(),
        })

        return render(request, 'home-with-profile.html', context)

    if request.method == 'GET':
        form = ProfileForm()

    else:
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')

    context.update(
        {"form": form}
    )

    return render(request, 'home-no-profile.html', context)
