from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['company', 'contact', 'message',]

        widgets = {
            'company': forms.TextInput(attrs={'size': 50}),
            'contact': forms.TextInput(attrs={'size': 50}),
            'message': forms.TextInput(attrs={'size': 50}),
        }


