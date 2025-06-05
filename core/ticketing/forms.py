from django import forms
from .models import TicketInformation

class TicketForm(forms.ModelForm):
    class Meta:
        model = TicketInformation
        fields = ['title', 'text']
        labels = {
            'title': 'عنوان',
            'text': 'متن پیام',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
