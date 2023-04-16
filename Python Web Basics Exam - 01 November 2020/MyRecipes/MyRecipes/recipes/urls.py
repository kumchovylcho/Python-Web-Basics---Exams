from django.urls import path

from MyRecipes.recipes.views import index, create, edit, delete, details

urlpatterns = (
    path('', index, name='index'),
    path('create', create, name='create'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete'),
    path('details/<int:pk>', details, name='details'),

)