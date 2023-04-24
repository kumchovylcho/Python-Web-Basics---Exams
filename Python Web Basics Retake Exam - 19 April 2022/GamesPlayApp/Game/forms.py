from django import forms

from GamesPlayApp.Game.models import BaseGame


class BaseGameForm(forms.ModelForm):

    class Meta:
        model = BaseGame
        fields = "__all__"
