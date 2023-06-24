from django.contrib import admin
from django.urls import (path,
                         include,
                         )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("web_basics.common.urls")),
    path("", include("web_basics.Fruit.urls")),
    path("profile/", include("web_basics.Profile.urls")),
]
