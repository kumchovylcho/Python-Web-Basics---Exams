from django.shortcuts import render, redirect

from NotesApp.User.forms import BaseForm
from NotesApp.User.models import User
from NotesApp.Notes.models import Note


def create_profile(request):
    profile = User.objects.all()
    notes = Note.objects.all()

    if request.method == "GET":
        form = BaseForm()

    else:
        form = BaseForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('view_profile')

    context = {'form': form,
               'profile': profile,
               'notes': notes,
               }

    return render(request, 'home-with-profile.html', context)


def view_profile(request):
    user = User.objects.get()
    notes = Note.objects.all()

    context = {
        'user': user,
        'all_notes': len(notes)
    }

    return render(request, 'profile.html', context)


def delete_profile(request):
    user = User.objects.get()
    user_notes = Note.objects.all()

    for note in user_notes:
        note.delete()

    user.delete()

    return redirect('create_profile')
