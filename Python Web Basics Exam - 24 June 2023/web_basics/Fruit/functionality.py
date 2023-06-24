from django import forms


def generate_placeholders(fields):
    result = {}

    bridge = {
        "name": {"placeholder": "Fruit Name", "type": forms.TextInput},
        "image_url": {"placeholder": "Fruit Image URL", "type": forms.TextInput},
        "description": {"placeholder": "Fruit Description", "type": forms.Textarea},
        "nutrition": {"placeholder": "Nutrition Info", "type": forms.Textarea},
    }
    for field in fields[1:]:
        field = field.name

        placeholder = bridge[field]["placeholder"]
        field_type = bridge[field]["type"]

        result[field] = field_type(
            attrs={
                "placeholder": placeholder
            }
        )

    return result
