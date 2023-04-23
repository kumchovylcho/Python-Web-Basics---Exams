from django import forms

from MusicApp.Album.models import BaseAlbum


def album_placeholders():
    placeholders = {}

    for field in BaseAlbum._meta.get_fields()[1:]:
        if field.name == "genre":
            continue

        atr = field.name.split("_")

        placeholders[field.name] = forms.TextInput(
            attrs={
                'placeholder': " ".join(
                    x.capitalize() if x.lower() != "url" else x.upper() for x in atr
                )
            }
        )

    return placeholders


class AlbumForm(forms.ModelForm):

    class Meta:
        model = BaseAlbum
        fields = "__all__"
        widgets = album_placeholders()