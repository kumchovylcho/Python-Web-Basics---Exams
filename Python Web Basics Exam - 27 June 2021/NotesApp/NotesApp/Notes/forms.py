from django.forms import ModelForm

from NotesApp.Notes.models import Note


class BaseNote(ModelForm):

    class Meta:
        model = Note
        fields = "__all__"
