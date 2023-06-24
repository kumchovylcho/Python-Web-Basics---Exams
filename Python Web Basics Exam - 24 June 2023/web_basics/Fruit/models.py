from django.core.validators import MinLengthValidator
from django.db import models

from web_basics.Fruit.validators import check_if_alpha


class Fruit(models.Model):
    NAME_MAX_LETTERS = 30
    NAME_MIN_LETTERS = 2

    name = models.CharField(
        blank=False,
        null=False,
        max_length=NAME_MAX_LETTERS,
        validators=(MinLengthValidator(NAME_MIN_LETTERS),
                    check_if_alpha,
                    ),
        )

    image_url = models.URLField(
        blank=False,
        null=False,
        )

    description = models.TextField(
        blank=False,
        null=False,
        )

    nutrition = models.TextField(
        blank=True,
        null=True,
        )
