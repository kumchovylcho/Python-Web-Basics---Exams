from django import forms

from CarCollectionApp.Car.models import BaseCar


class BaseCarForm(forms.ModelForm):

    class Meta:
        model = BaseCar
        fields = "__all__"
