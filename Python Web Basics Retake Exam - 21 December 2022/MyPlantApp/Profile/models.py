from django.db import models
from django.core.validators import MinLengthValidator
from MyPlantApp.Profile.validators import validate_name


class BaseProfile(models.Model):
    USERNAME_MAX_LENGTH = 10
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MAX_LENGTH = 20

    username = models.CharField(
        blank=False,
        null=False,
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(2),
        )
    )

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            validate_name,
        )
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            validate_name,
        )
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )