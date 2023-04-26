from django import forms

from MyPlantApp.Plant.models import BasePlant


class BasePlantForm(forms.ModelForm):

    class Meta:
        model = BasePlant
        fields = "__all__"
