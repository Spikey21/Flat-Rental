from django import forms
from .models import Message


class ChatForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['participants',]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['chat', 'text']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
