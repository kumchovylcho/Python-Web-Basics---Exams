from django.core.exceptions import ValidationError


def start_with_letter(string: str):
    if not string[0].isalpha():
        raise ValidationError("Your name must start with a letter!")