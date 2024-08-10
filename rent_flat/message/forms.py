from django import forms
from django.contrib.auth import get_user_model
from django.forms import modelformset_factory

from .models import Message, Chat

User = get_user_model()


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
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


MessageFormSet = modelformset_factory(Message, form=MessageForm, extra=1)
