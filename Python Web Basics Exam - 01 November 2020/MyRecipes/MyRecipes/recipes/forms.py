from django.forms import ModelForm
from MyRecipes.recipes.models import Recipe


class RecipeBaseForm(ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"

