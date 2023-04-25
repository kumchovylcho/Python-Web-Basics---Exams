from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('CarCollectionApp.common.urls')),
    path("", include('CarCollectionApp.Car.urls')),
    path('profile/', include('CarCollectionApp.Profile.urls')),
]
