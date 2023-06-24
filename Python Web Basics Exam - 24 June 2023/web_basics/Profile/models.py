from django.core.validators import MinLengthValidator
from django.db import models

from web_basics.Profile.validators import start_with_letter


class Profile(models.Model):
    FIRST_NAME_MAX_SYMBOLS = 25
    FIRST_NAME_MIN_SYMBOLS = 2

    LAST_NAME_MAX_SYMBOLS = 35
    LAST_NAME_MIN_SYMBOLS = 1

    EMAIL_MAX_SYMBOLS = 40

    PASSWORD_MAX_SYMBOLS = 20
    PASSWORD_MIN_SYMBOLS = 8

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=FIRST_NAME_MAX_SYMBOLS,
        validators=(start_with_letter,
                    MinLengthValidator(FIRST_NAME_MIN_SYMBOLS),
                    ),
        )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=LAST_NAME_MAX_SYMBOLS,
        validators=(start_with_letter,
                    MinLengthValidator(LAST_NAME_MIN_SYMBOLS),
                    ),
        )

    email = models.EmailField(
        blank=False,
        null=False,
        max_length=EMAIL_MAX_SYMBOLS,
        )

    password = models.CharField(
        blank=False,
        null=False,
        max_length=PASSWORD_MAX_SYMBOLS,
        validators=(MinLengthValidator(PASSWORD_MIN_SYMBOLS),
                    ),
        )

    image_url = models.URLField(
        blank=True,
        null=True,
        )

    age = models.IntegerField(
        blank=True,
        null=True,
        default=18,
        )