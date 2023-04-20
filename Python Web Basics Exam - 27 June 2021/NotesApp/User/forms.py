from django.forms import ModelForm

from NotesApp.User.models import User


class BaseForm(ModelForm):

    class Meta:
        model = User
        fields = "__all__"
