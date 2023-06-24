from django import forms

from web_basics.Profile.models import Profile


def get_profile():
    try:
        return Profile.objects.first()

    except Profile.DoesNotExist:
        return


def generate_placeholders(fields):
    result = {}

    for field in fields:
        if field == "password":
            result[field] = forms.PasswordInput(
                attrs={
                    "placeholder": field.capitalize()
                }
            )
            continue

        result[field] = forms.TextInput(
            attrs={
                "placeholder": " ".join(x.capitalize() for x in field.split("_"))
            }
        )

    return result


