from django.shortcuts import render, redirect

from web_basics.Fruit.forms import CreateFruit, EditFruit, DeleteFruit
from web_basics.Fruit.models import Fruit
from web_basics.Profile.functionality import get_profile


def create_fruit(request):
    form = CreateFruit()

    if request.method == 'POST':
        form = CreateFruit(request.POST)

        if form.is_valid():
            form.save()

            return redirect("dashboard")

    context = {
        "profile": get_profile(),
        "form": form,
    }

    return render(request, "create-fruit.html", context)


def fruit_details(request, pk):
    context = {
        "profile": get_profile(),
        "fruit": Fruit.objects.get(pk=pk),
    }

    return render(request, "details-fruit.html", context)


def edit_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    form = EditFruit(instance=fruit)

    if request.method == "POST":
        form = EditFruit(request.POST, instance=fruit)

        if form.is_valid():
            form.save()

            return redirect("dashboard")

    context = {
        "profile": get_profile(),
        "fruit": fruit,
        "form": form,
    }

    return render(request, "edit-fruit.html", context)


def delete_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    form = DeleteFruit(instance=fruit)

    if request.method == "POST":
        form = DeleteFruit(request.POST, instance=fruit)
        form.save()

        return redirect("dashboard")

    context = {
        "profile": get_profile(),
        "fruit": fruit,
        "form": form,
    }

    return render(request, "delete-fruit.html", context)