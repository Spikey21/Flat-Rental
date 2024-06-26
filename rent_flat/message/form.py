from django import forms
from .models import Message


class ChatForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name','participants']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'placeholder': 'Type your message...'})
        super(MessageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
