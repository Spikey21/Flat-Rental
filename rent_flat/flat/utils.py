from datetime import date

from django.core.exceptions import ValidationError
from django.forms import DateField, IntegerField


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


def positive_validator(value):
    if value < 0:
        raise ValidationError('Value must be positive.')


class YearField(IntegerField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today().year:
            raise ValidationError('Future years not allowed here.')

