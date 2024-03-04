import django_filters
from django import forms
from django_filters import RangeFilter, MultipleChoiceFilter, ModelMultipleChoiceFilter, ChoiceFilter, ModelChoiceFilter

from .models import Flat, FlatLocation, FlatDetail


class FlatFilter(django_filters.FilterSet):
    price = RangeFilter()
    area = RangeFilter()
    detail = ModelChoiceFilter(queryset=FlatDetail.objects.all(), label='FlatDetail', distinct=True)
    year = RangeFilter()
    location = ModelChoiceFilter(queryset=FlatLocation.objects.all(), label='FlatLocation', distinct=True)

    class Meta:
        model = Flat
        fields = ['price', 'area', 'detail__rooms', 'detail__development_type', 'year', 'location__city']
