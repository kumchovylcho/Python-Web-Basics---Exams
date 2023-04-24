from django.urls import path

from GamesPlayApp.Game.views import (create_game,
                                     game_details,
                                     edit_game,
                                     delete_game,
                                     )

urlpatterns = (
    path('create/', create_game, name='create_game'),
    path('details/<int:pk>/', game_details, name='game_details'),
    path('edit/<int:pk>/', edit_game, name='edit_game'),
    path('delete/<int:pk>/', delete_game, name='delete_game')
)