from django.db import models
from django.core.validators import (MinLengthValidator,
                                    MinValueValidator,
                                    MaxValueValidator
                                    )


class BaseCar(models.Model):
    TYPE_MAX_LENGTH = 10
    MODEL_MAX_LENGTH = 20

    YEAR_ERROR_MESSAGE = "Year must be between 1980 and 2049"

    type = models.CharField(
        blank=False,
        null=False,
        max_length=TYPE_MAX_LENGTH,
        choices=(
            ("Sports Car", "Sports Car"),
            ("Pickup", "Pickup"),
            ("Crossover", "Crossover"),
            ("Minibus", "Minibus"),
            ("Other", "Other"),
        )
    )

    model = models.CharField(
        blank=False,
        null=False,
        max_length=MODEL_MAX_LENGTH,
        validators=(
            MinLengthValidator(2),
        )
    )

    year = models.IntegerField(
        blank=False,
        null=False,
        validators=(
            MinValueValidator(1980, message=YEAR_ERROR_MESSAGE),
            MaxValueValidator(2049, message=YEAR_ERROR_MESSAGE),
        )
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=(
            MinValueValidator(1),
        )
    )