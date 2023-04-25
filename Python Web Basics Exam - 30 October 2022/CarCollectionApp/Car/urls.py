from django.urls import path

from CarCollectionApp.Car.views import (show_catalogue,
                                        create_car,
                                        car_details,
                                        edit_car,
                                        delete_car,
                                        )

urlpatterns = (
    path('catalogue/', show_catalogue, name='show_catalogue'),
    path('car/create/', create_car, name='create_car'),
    path('car/<int:pk>/details/', car_details, name='car_details'),
    path('car/<int:pk>/edit/', edit_car, name='edit_car'),
    path('car/<int:pk>/delete/', delete_car, name='delete_car'),
)