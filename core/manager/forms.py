from django import forms
from .models import ManagerInformation, DocumentManager

class ManagerProfileForm(forms.ModelForm):
    class Meta:
        model = ManagerInformation
        fields = ['phone_number1', 'phone_number2', 'address', 'address2']
        labels = {
            'phone_number1': 'شماره تماس اول',
            'phone_number2': 'شماره تماس دوم',
            'address': 'استان',
            'address2': 'جزئیات آدرس',
        }
        widgets = {
            'address2': forms.Textarea(attrs={'rows': 3}),
        }

class ManagerDocumentsForm(forms.ModelForm):
    class Meta:
        model = DocumentManager
        fields = ['doc1', 'doc2', 'doc3', 'doc4']
        labels = {
            'doc1': 'سند 1 احراز هویت کاربری',
            'doc2': 'سند 2 احراز هویت کاربری',
            'doc3': 'سند 3 احراز هویت کاربری',
            'doc4': 'سند 4 احراز هویت کاربری',
        }