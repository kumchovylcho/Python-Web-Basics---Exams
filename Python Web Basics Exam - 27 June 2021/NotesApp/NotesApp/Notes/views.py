from django.shortcuts import render, redirect

from NotesApp.Notes.forms import BaseNote
from NotesApp.Notes.models import Note


def disable_fields(form):
    for field in form.fields.values():
        field.widget.attrs['disabled'] = 'disabled'


def add_note(request):
    if request.method == "GET":
        form = BaseNote()

    else:
        form = BaseNote(request.POST)

        if form.is_valid():
            form.save()

            return redirect('create_profile')

    context = {
        'form': form,
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = BaseNote(instance=note)

    else:
        form = BaseNote(request.POST, instance=note)

        if form.is_valid():
            form.save()

            return redirect('create_profile')

    context = {
        'note': note,
        'form': form,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    form = BaseNote(instance=note)

    if request.method == "GET":
        disable_fields(form)

    else:
        note.delete()

        return redirect('create_profile')

    context = {
        'note': note,
        'form': form,
    }

    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.filter(pk=pk).get()

    context = {
        'note': note,
    }

    return render(request, 'note-details.html', context)
