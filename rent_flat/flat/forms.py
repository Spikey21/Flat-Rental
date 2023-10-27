from django import forms
from django.forms import inlineformset_factory

from .models import Flat, FlatImage, Equip, FlatLocation


class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        exclude = ('created_at', 'user', 'status')


class EquipForm(forms.ModelForm):
    class Meta:
        model = Equip
        fields = ('name',)


class LocationForm(forms.ModelForm):
    class Meta:
        model = FlatLocation
        fields = ('province', 'county', 'city')


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class FlatImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = FlatImage
        fields = ('image',)
        widgets = {
            'image': MultipleFileInput()
        }


ImageInlineFormSet = inlineformset_factory(Flat, FlatImage, form=FlatImageForm, extra=9)
