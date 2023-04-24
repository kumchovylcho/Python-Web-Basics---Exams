from django.db import models
from django.core.validators import MinValueValidator


class BaseProfile(models.Model):

    email = models.EmailField(
        blank=False,
        null=False,
        verbose_name="Email"
    )

    age = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="Age",
        validators=(
            MinValueValidator(12),
        )
    )

    password = models.CharField(
        blank=False,
        null=False,
        verbose_name="Password",
        max_length=30
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        verbose_name="First Name",
        max_length=30
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        verbose_name="Last Name",
        max_length=30
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name="Profile Picture",
    )