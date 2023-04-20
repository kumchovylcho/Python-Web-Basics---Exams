from django.db import models


class BaseBook(models.Model):
    TITLE_MAX_CHARACTERS = 30
    TYPE_BOOK_MAX_CHARACTERS = 30

    title = models.CharField(
        max_length=TITLE_MAX_CHARACTERS
    )

    description = models.TextField()

    image = models.URLField()

    type = models.CharField(
        max_length=TYPE_BOOK_MAX_CHARACTERS
    )

