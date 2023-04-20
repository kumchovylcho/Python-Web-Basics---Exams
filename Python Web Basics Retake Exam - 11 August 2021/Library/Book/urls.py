from django.urls import path

from Library.Book.views import add_book, edit_book, book_details, delete_book

urlpatterns = (
    path("add/", add_book, name="add_book"),
    path("edit/<int:pk>", edit_book, name="edit_book"),
    path("details/<int:pk>", book_details, name="book_details"),
    path("details/delete/<int:pk>", delete_book, name="delete_book"),
)
