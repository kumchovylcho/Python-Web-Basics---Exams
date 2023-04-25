from django.urls import path

from CarCollectionApp.common.views import index

urlpatterns = (
    path("", index, name='index'),
)