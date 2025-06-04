from django import forms
from .models import StudentInformation, Document_Authenticate_Student, Document_Education_Student

# فرم پروفایل دانش آموز
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentInformation
        fields = ['phone', 'address']
        labels = {
            'phone': 'شماره تماس',
            'address': 'استان'
        }

# فرم مدارک هویتی
class StudentAuthenticationDocumentForm(forms.ModelForm):
    class Meta:
        model = Document_Authenticate_Student
        fields = ['doc1', 'doc2', 'doc3']

# فرم مدارک تحصیلی
class StudentEducationDocumentForm(forms.ModelForm):
    class Meta:
        model = Document_Education_Student
        fields = ['file1', 'file2', 'file3', 'file4', 'file5', 'file6', 'file7', 'file8', 'file9', 'file10', 'file11', 'file12']






