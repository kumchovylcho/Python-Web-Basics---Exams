from django.urls import path

from MyPlantApp.Plant.views import (create_plant,
                                    show_catalogue,
                                    plant_details,
                                    edit_plant,
                                    delete_plant,
                                    )

urlpatterns = (
    path('create/', create_plant, name='create_plant'),
    path('catalogue/', show_catalogue, name='show_catalogue'),
    path('details/<int:pk>', plant_details, name='plant_details'),
    path('edit/<int:pk>', edit_plant, name='edit_plant'),
    path('delete/<int:pk>', delete_plant, name='delete_plant'),
)