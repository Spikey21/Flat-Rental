from django.core.exceptions import ValidationError


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


def positive_validator(value):
    if value < 0:
        raise ValidationError('Value must be positive.')
