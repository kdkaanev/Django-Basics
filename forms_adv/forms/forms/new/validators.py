from django.core.exceptions import ValidationError


def validate_name(value):
    if " " in value:
        raise ValidationError("Name cannot contain spaces")