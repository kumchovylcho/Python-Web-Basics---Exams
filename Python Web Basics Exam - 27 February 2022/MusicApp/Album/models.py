from django.db import models
from django.core.validators import MinValueValidator


class BaseAlbum(models.Model):

    album_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=30,
        verbose_name="Album Name"
    )

    artist = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        verbose_name="Artist"
    )

    genre = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=(
            ("Pop Music", "Pop Music"),
            ("Jazz Music", "Jazz Music"),
            ("R&B Music", "R&B Music"),
            ("Rock Music", "Rock Music"),
            ("Country Music", "Country Music"),
            ("Dance Music", "Dance Music"),
            ("Hip Hop Music", "Hip Hop Music"),
            ("Other", "Other"),
        ),
        verbose_name="Genre",
    )

    description = models.TextField(
        verbose_name="Description",
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name="Image URL",
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=(
            MinValueValidator(0),
        )
    )

