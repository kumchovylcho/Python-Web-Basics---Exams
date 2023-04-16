from django.db import models


class Recipe(models.Model):
    MAX_TITLE_CHARS = 30
    MAX_INGREDIENT_CHARACTERS = 250

    title = models.CharField(
        max_length=MAX_TITLE_CHARS
    )

    image_url = models.URLField(
        verbose_name="Image URL",
    )

    description = models.TextField()

    ingredients = models.CharField(
        max_length=MAX_INGREDIENT_CHARACTERS
    )

    time = models.IntegerField(
        verbose_name="Time(Minutes)",
    )