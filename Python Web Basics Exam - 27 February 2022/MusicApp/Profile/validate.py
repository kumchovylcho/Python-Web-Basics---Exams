from django.core.exceptions import ValidationError
import re


def validate_username(name):
    pattern = re.compile(r'^\w+$')

    match = list(pattern.finditer(name))

    if not match:
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")

