from django import forms

from CarCollectionApp.Profile.models import BaseProfile


class BaseProfileForm(forms.ModelForm):

    class Meta:
        model = BaseProfile
        fields = "__all__"


class CreateProfileForm(BaseProfileForm):

    class Meta:
        model = BaseProfile
        fields = ("username", "email", "age", "password")
        widgets = {
            'password': forms.PasswordInput()
        }