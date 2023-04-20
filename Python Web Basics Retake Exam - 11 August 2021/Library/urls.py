from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('Library.Book.urls')),
    path("", include('Library.Profile.urls')),
    path("", include('Library.common.urls'))
]
