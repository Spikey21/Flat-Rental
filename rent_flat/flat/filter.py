import django_filters
from django_filters import RangeFilter, MultipleChoiceFilter

from .models import Flat


class FlatFilter(django_filters.FilterSet):
    price = RangeFilter()
    area = RangeFilter()
    rooms = MultipleChoiceFilter()
    year = RangeFilter()
    equipment = MultipleChoiceFilter()

    class Meta:
        model = Flat
        fields = ['price', 'area', 'rooms', 'development_type', 'year', 'equipment']
