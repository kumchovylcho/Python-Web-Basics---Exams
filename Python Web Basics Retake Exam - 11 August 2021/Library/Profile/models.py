from django.db import models


class BaseProfile(models.Model):
    FIRST_NAME_MAX_CHARACTERS = 30
    LAST_NAME_MAX_CHARACTERS = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_CHARACTERS
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_CHARACTERS
    )

    image_url = models.URLField()