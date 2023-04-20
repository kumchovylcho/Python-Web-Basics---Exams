from django.urls import path

from NotesApp.User.views import view_profile, create_profile, delete_profile

urlpatterns = (
    path("", create_profile, name='create_profile'),
    path("profile/", view_profile, name='view_profile'),
    path("profile/delete", delete_profile, name="delete_profile"),
)