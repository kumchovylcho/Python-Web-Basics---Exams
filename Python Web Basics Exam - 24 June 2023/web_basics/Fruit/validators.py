from django.core.exceptions import ValidationError


def check_if_alpha(value: str):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")