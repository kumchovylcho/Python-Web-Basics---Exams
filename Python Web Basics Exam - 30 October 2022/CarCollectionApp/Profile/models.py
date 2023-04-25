from django.db import models
from django.core.validators import (MinLengthValidator,
                                    MinValueValidator,
                                    )


class BaseProfile(models.Model):
    USERNAME_MAX_LENGTH = 10
    USERNAME_ERROR_MESSAGE = "The username must be a minimum of 2 chars"

    PASSWORD_MAX_LENGTH = 30

    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    username = models.CharField(
        blank=False,
        null=False,
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(2, message=USERNAME_ERROR_MESSAGE),
        ),
        verbose_name="UserNAME"
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        blank=False,
        null=False,
        validators=(
            MinValueValidator(18),
        )
    )

    password = models.CharField(
        blank=False,
        null=False,
        max_length=PASSWORD_MAX_LENGTH
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=FIRST_NAME_MAX_LENGTH
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=LAST_NAME_MAX_LENGTH
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )