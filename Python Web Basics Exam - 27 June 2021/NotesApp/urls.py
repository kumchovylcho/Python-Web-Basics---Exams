from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('NotesApp.Notes.urls')),
    path("", include('NotesApp.User.urls')),
]
