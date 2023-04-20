from django.shortcuts import render, redirect

from MyRecipes.recipes.models import Recipe
from MyRecipes.recipes.forms import RecipeBaseForm


def index(request):
    recipe = Recipe.objects.all()

    context = {
        'recipe': recipe
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == "GET":
        form = RecipeBaseForm()

    else:
        form = RecipeBaseForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'create.html', context)


def edit(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = RecipeBaseForm(instance=recipe)

    else:
        form = RecipeBaseForm(request.POST, instance=recipe)

        if form.is_valid():
            recipe.save()

            return redirect('index')

    context = {
        'form': form,
        'recipe': recipe
    }
    return render(request, 'edit.html', context)


def delete(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    form = RecipeBaseForm(instance=recipe)

    if request.method == "GET":
        for field in form.fields.values():
            field.widget.attrs['disabled'] = 'disabled'

    else:
        recipe.delete()

        return redirect('index')

    context = {
        'form': form,
        'recipe': recipe
    }

    return render(request, 'delete.html', context)


def details(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()

    context = {
        'recipe': recipe,
        'ingredients': recipe.ingredients.split(", ")
    }

    return render(request, 'details.html', context)