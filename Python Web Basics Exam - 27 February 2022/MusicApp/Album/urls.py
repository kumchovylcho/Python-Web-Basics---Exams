from django.urls import path

from MusicApp.Album.views import add_album, album_details, edit_album, delete_album, index

urlpatterns = (
    path("", index, name="index"),
    path("album/add", add_album, name="add_album"),
    path("album/details/<int:pk>", album_details, name="album_details"),
    path("album/edit/<int:pk>", edit_album, name="edit_album"),
    path("album/delete/<int:pk>", delete_album, name="delete_album"),
)