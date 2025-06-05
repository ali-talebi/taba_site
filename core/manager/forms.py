from django import forms
from .models import ManagerInformation, DocumentManager
from school.models import  SchoolInformation, Level_Education_School, Field_Education_School 


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
            'address': forms.Select(attrs={'class': 'form-select'}) , 
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
        
        
class SchoolInformationForm(forms.ModelForm):
    class Meta:
        model = SchoolInformation
        fields = ['school_name', 'logo', 'address']
        labels = {
            'school_name': 'نام مدرسه',
            'logo': 'لوگوی مدرسه',
            'address': 'استان',
        }
        widgets = {
            'address': forms.Select(attrs={'class': 'form-select'}),
        }

        
class LevelEducationForm(forms.ModelForm):
    fields = forms.ModelMultipleChoiceField(
        queryset=Field_Education_School.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='رشته‌های تحصیلی'
    )

    class Meta:
        model = Level_Education_School
        fields = ['name_level', 'fields']
        labels = {
            'name_level': 'نام سطح تحصیلی',
        }