from django import forms
from django.forms import inlineformset_factory

from .models import Flat, FlatImage, FlatLocation, FlatDetail


class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        exclude = ('created_at', 'user', 'status')


class UpdateFlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        exclude = ('created_at', 'user')


class DetailForm(forms.ModelForm):
    class Meta:
        model = FlatDetail
        exclude = ('flat',)

    def __init__(self, *args, **kwargs):
        super(DetailForm, self).__init__(*args, **kwargs)
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


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class FlatImageForm(forms.ModelForm):
    image = forms.ImageField(label='image')

    class Meta:
        model = FlatImage
        fields = ('image',)
        widgets = {
            'image': MultipleFileInput(attrs={'class':'form-control',
                                              'type' : 'file'})
        }

    def __init__(self, *args, **kwargs):
        super(FlatImageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


ImageInlineFormSet = inlineformset_factory(Flat, FlatImage, form=FlatImageForm, extra=12)
LocationInlineFormSet = inlineformset_factory(Flat, FlatLocation, form=LocationForm, extra=1)

