from django.shortcuts import render, redirect

from Library.Book.forms import BookForm
from Library.Book.models import BaseBook
from Library.Profile.models import BaseProfile


def add_book(request):
    if request.method == "GET":
        form = BookForm()

    else:
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'form': form,
        'profile': BaseProfile.objects.get()
    }

    return render(request, 'add-book.html', context)


def book_details(request, pk):
    book = BaseBook.objects.filter(pk=pk).get()

    context = {
        'book': book,
        'profile': BaseProfile.objects.get(),
    }

    return render(request, 'book-details.html', context)


def edit_book(request, pk):
    book = BaseBook.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = BookForm(instance=book)

    else:
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'form': form,
        'profile': BaseProfile.objects.get(),
        'book': book,
    }

    return render(request, 'edit-book.html', context)


def delete_book(request, pk):
    BaseBook.objects.filter(pk=pk).get().delete()

    return redirect('index')
