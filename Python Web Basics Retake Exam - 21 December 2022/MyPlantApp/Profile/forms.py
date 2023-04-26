from django import forms

from MyPlantApp.Profile.models import BaseProfile


class BaseProfileForm(forms.ModelForm):

    class Meta:
        model = BaseProfile
        fields = "__all__"


class CreateProfileForm(BaseProfileForm):

    class Meta:
        model = BaseProfile
        fields = ("username", "first_name", "last_name")
