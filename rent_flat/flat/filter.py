import django_filters
from django import forms
from django_filters import RangeFilter, MultipleChoiceFilter, ModelMultipleChoiceFilter, ChoiceFilter, \
    ModelChoiceFilter, AllValuesMultipleFilter

from .models import Flat, FlatLocation, FlatDetail


class FlatFilter(django_filters.FilterSet):
    price = RangeFilter()
    detail = ModelMultipleChoiceFilter(queryset=FlatDetail.objects.all(), label='FlatDetail', distinct=True)
    location = ModelChoiceFilter(queryset=FlatLocation.objects.all(), label='FlatLocation', distinct=True)

    class Meta:
        model = Flat
        fields = {"price": ["gte", "lte"],
                  'detail__area': ["gte", "lte"],
                  'detail__rooms': ["exact"],
                  'detail__development_type': ["exact"],
                  'detail__year': ["gte", "lte"],
                  'location__city': ["exact"],
                  }
