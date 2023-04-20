from django.urls import path

from Library.common.views import index

urlpatterns = (
    path("", index, name='index'),
)