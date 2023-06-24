from django.urls import (path,
                         include,
                         )
from .views import (create_fruit,
                    fruit_details,
                    edit_fruit,
                    delete_fruit,
                    )

urlpatterns = (
    path("create/", create_fruit, name="create_fruit"),
    path("<int:pk>/", include([
        path("details/", fruit_details, name="fruit_details"),
        path("edit/", edit_fruit, name="edit_fruit"),
        path("delete/", delete_fruit, name="delete_fruit"),
    ]))
)