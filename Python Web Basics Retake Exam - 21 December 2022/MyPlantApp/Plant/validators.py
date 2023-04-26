from django.core.exceptions import ValidationError


def validate_name(name):
    if not name.isalpha():
        raise ValidationError(
            "Plant name should contain only letters!"
        )