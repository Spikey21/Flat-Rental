import re

from django import forms
from django.forms import inlineformset_factory, CharField, Textarea, IntegerField, FloatField

from .models import Flat, FlatImage, FlatLocation, FlatDetail
from .utils import capitalized_validator, positive_validator


class FlatForm(forms.ModelForm):
    title = CharField(max_length=120, validators=[capitalized_validator])
    text = CharField(widget=Textarea)
    price = IntegerField(min_value=0, validators=[positive_validator])

    class Meta:
        model = Flat
        exclude = ('created_at', 'user', 'status')

    def clean_text(self):
        # Force each sentence of the text to be capitalized.
        initial = self.cleaned_data['text']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)


class UpdateFlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        fields = ('title', 'text', 'price', 'status', 'equipment')

    def __init__(self, *args, **kwargs):
        super(UpdateFlatForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class DetailForm(forms.ModelForm):
    area = FloatField(min_value=0.0, validators=[positive_validator])
    year = IntegerField(min_value=0, validators=[positive_validator])

    class Meta:
        model = FlatDetail
        exclude = ('flat',)

    def __init__(self, *args, **kwargs):
        super(DetailForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class DetailUpdateForm(forms.ModelForm):
    class Meta:
        model = FlatDetail
        exclude = ('flat',)

    def __init__(self, *args, **kwargs):
        super(DetailUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class LocationForm(forms.ModelForm):
    class Meta:
        model = FlatLocation
        fields = ('city', 'district', 'street')

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class UpdateLocationForm(forms.ModelForm):
    class Meta:
        model = FlatLocation
        fields = ('city', 'district', 'street')

    def __init__(self, *args, **kwargs):
        super(UpdateLocationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class FlatImageForm(forms.ModelForm):
    image = forms.ImageField(label='image')

    class Meta:
        model = FlatImage
        fields = ('image',)
        widgets = {
            'image': MultipleFileInput(attrs={'class': 'form-control',
                                              'type': 'file'})
        }

    def __init__(self, *args, **kwargs):
        super(FlatImageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ImageUpdateForm(forms.ModelForm):
    image = forms.ImageField(label='image')

    class Meta:
        model = FlatImage
        fields = ('image',)
        widgets = {
            'image': MultipleFileInput(attrs={'class': 'form-control',
                                              'type': 'file'})
        }


ImageInlineFormSet = inlineformset_factory(Flat, FlatImage, form=FlatImageForm, extra=12)
LocationInlineFormSet = inlineformset_factory(Flat, FlatLocation, form=LocationForm, extra=1)
DetailInlineFormSet = inlineformset_factory(Flat, FlatDetail, form=DetailForm, extra=1)

