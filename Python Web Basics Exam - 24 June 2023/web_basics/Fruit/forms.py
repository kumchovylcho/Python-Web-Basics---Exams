from django import forms

from web_basics.Fruit.functionality import generate_placeholders
from web_basics.Fruit.models import Fruit


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"


class CreateFruit(BaseFruitForm):
    class Meta:
        model = Fruit
        fields = "__all__"

        labels = {field.name: "" for field in model._meta.get_fields()}
        widgets = generate_placeholders(model._meta.get_fields())


class EditFruit(BaseFruitForm):
    class Meta:
        model = Fruit
        fields = "__all__"

        labels = {}

        bridge = {"image_url": "Image URL"}
        for field in model._meta.get_fields()[1:]:
            if field.name in bridge:
                labels[field.name] = bridge[field.name]
                break


class DeleteFruit(EditFruit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'

    def save(self, commit=True):
        if commit:
            self.instance.delete()

    class Meta:
        model = Fruit
        fields = ("name", "image_url", "description")

        labels = {}

        bridge = {"image_url": "Image URL"}
        for field in model._meta.get_fields()[1:]:
            if field.name in bridge:
                labels[field.name] = bridge[field.name]
                break
