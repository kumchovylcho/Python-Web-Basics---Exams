from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator

from MusicApp.Profile.validate import validate_username


class BaseProfile(models.Model):

    username = models.CharField(
        blank=False,
        null=False,
        max_length=15,
        validators=(
            MinLengthValidator(2),
            validate_username,
        ),
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(0),
        )
    )