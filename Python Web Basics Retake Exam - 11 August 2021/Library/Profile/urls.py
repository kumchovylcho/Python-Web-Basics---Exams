from django.urls import path

from Library.Profile.views import view_profile, edit_profile, delete_profile

urlpatterns = (
    path("profile/", view_profile, name="view_profile"),
    path("profile/edit/", edit_profile, name="edit_profile"),
    path("profile/delete/", delete_profile, name="delete_profile"),
)