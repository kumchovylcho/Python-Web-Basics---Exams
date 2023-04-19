from django.db import models


class User(models.Model):
    FIRST_NAME_MAX_CHARACTERS = 20
    LAST_NAME_MAX_CHARACTERS = 20

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_CHARACTERS
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_CHARACTERS
    )

    age = models.IntegerField()

    image_url = models.URLField()
