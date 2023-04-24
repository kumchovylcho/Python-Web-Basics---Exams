from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('GamesPlayApp.common.urls')),
    path("game/", include('GamesPlayApp.Game.urls')),
    path("profile/", include('GamesPlayApp.Profile.urls')),
]
