from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class BaseGame(models.Model):

    title = models.CharField(
        blank=False,
        null=False,
        verbose_name="Title",
        unique=True,
        max_length=30
    )

    category = models.CharField(
        blank=False,
        null=False,
        verbose_name="Category",
        max_length=15,
        choices=(
            ("Action", "Action"),
            ("Adventure", "Adventure"),
            ("Puzzle", "Puzzle"),
            ("Strategy", "Strategy"),
            ("Sports", "Sports"),
            ("Board/Card Game", "Board/Card Game"),
            ("Other", "Other"),
        )
    )

    rating = models.FloatField(
        blank=False,
        null=False,
        verbose_name="Rating",
        validators=(
            MinValueValidator(0.1),
            MaxValueValidator(5.0),
        )
    )

    max_level = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Max Level",
        validators=(
            MinValueValidator(1),
        )
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name="Image URL",
    )

    summary = models.TextField(
        blank=True,
        null=True,
        verbose_name="Summary",
    )