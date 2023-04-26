from django.urls import path

from MyPlantApp.common.views import index

urlpatterns = (
    path("", index, name='index'),
)