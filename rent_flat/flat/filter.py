import django_filters
from django import forms
from django_filters import RangeFilter, MultipleChoiceFilter, ModelMultipleChoiceFilter, ChoiceFilter, ModelChoiceFilter

from .models import Flat, Room, FlatLocation


class FlatFilter(django_filters.FilterSet):
    price = RangeFilter()
    area = RangeFilter()
    rooms = ModelMultipleChoiceFilter(queryset=Room.objects.all(), widget=forms.CheckboxSelectMultiple())
    year = RangeFilter()

    class Meta:
        model = Flat
        fields = ['price', 'area', 'rooms', 'development_type', 'year', 'location__city']
