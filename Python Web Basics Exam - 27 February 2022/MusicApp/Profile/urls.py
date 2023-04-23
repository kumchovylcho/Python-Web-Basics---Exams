from django.urls import path

from MusicApp.Profile.views import profile_details, delete_profile

urlpatterns = (
    path("details/", profile_details, name="profile_details"),
    path("delete/", delete_profile, name="delete_profile"),
)