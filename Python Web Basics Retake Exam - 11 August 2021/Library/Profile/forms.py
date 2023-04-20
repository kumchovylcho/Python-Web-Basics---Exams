from django.forms import ModelForm

from Library.Profile.models import BaseProfile


class ProfileForm(ModelForm):

    class Meta:
        model = BaseProfile
        fields = "__all__"
