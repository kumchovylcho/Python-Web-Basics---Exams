from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('MusicApp.Album.urls')),
    path("profile/", include('MusicApp.Profile.urls')),
]
