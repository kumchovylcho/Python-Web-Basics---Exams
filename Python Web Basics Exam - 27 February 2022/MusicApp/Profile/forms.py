from django import forms

from MusicApp.Profile.models import BaseProfile


def user_placeholders():
    placeholders = {}

    for field in BaseProfile._meta.get_fields()[1:]:
        placeholders[field.name] = forms.TextInput(
            attrs={
                'placeholder': field.name.capitalize()
            }
        )

    return placeholders


class ProfileForm(forms.ModelForm):

    class Meta:
        model = BaseProfile
        fields = "__all__"
        widgets = user_placeholders()
