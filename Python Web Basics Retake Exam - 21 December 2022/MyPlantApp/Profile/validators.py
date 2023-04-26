from django.core.exceptions import ValidationError


def validate_name(name):
    if not name[0].isupper():
        raise ValidationError(
            "Your name must start with a capital letter!"
        )