from django.shortcuts import render, redirect

from Library.Book.models import BaseBook
from Library.Profile.forms import ProfileForm
from Library.Profile.models import BaseProfile


def disable_fields(form):
    for field in form.fields.values():
        field.widget.attrs['disabled'] = "disabled"


def view_profile(request):
    context = {
        "profile": BaseProfile.objects.get()
    }

    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = BaseProfile.objects.get()

    if request.method == 'GET':
        form = ProfileForm(instance=profile)

    else:
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()

            return redirect('view_profile')

    context = {
        "profile": profile,
        "form": form,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = BaseProfile.objects.get()

    if request.method == "GET":
        form = ProfileForm(instance=profile)

        disable_fields(form)

    else:
        profile.delete()
        BaseBook.objects.all().delete()

        return redirect('index')

    context = {
        "profile": profile,
        "form": form,
    }

    return render(request, "delete-profile.html", context)
