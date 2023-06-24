from django import forms

from web_basics.Fruit.models import Fruit
from web_basics.Profile.functionality import generate_placeholders
from web_basics.Profile.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class CreateProfile(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "email", "password")

        labels = {field: "" for field in fields}
        widgets = generate_placeholders(fields)


class EditProfile(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "image_url", "age")

        labels = {}

        for field in fields:
            if "url" in field:
                labels[field] = "Image URL"
                continue

            labels[field] = " ".join(field.capitalize() for field in field.split("_"))


class DeleteProfile(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Fruit.objects.all().delete()