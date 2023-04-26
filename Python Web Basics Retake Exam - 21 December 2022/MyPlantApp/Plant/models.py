from django.db import models
from django.core.validators import MinLengthValidator
from MyPlantApp.Plant.validators import validate_name


class BasePlant(models.Model):
    PLANT_TYPE_MAX_LENGTH = 14
    NAME_MAX_LENGTH = 20

    plant_type = models.CharField(
        blank=False,
        null=False,
        max_length=PLANT_TYPE_MAX_LENGTH,
        choices=(
            ("Outdoor Plants", "Outdoor Plants"),
            ("Indoor Plants", "Indoor Plants"),
        )
    )

    name = models.CharField(
        blank=False,
        null=False,
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(2),
            validate_name,
        )
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
    )