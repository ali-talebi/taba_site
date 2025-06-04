# enrollments/forms.py

from django import forms
from .models import Enrollment
from school.models import Field_Education_School, Level_Education_School

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['grade', 'academic_year', 'field']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # اضافه کردن کلاس‌های css به فیلدها
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'custom-select',
                'autocomplete': 'off',
            })

        # فیلتر کردن فیلد رشته تحصیلی بر اساس مقطع تحصیلی انتخاب شده
        if 'grade' in self.data:
            try:
                grade_id = int(self.data.get('grade'))
                self.fields['field'].queryset = Field_Education_School.objects.filter(level_education_school_id=grade_id).order_by('field_name')
            except (ValueError, TypeError):
                self.fields['field'].queryset = Field_Education_School.objects.none()
        elif self.instance.pk:
            self.fields['field'].queryset = Field_Education_School.objects.filter(level_education_school=self.instance.grade).order_by('field_name')
        else:
            self.fields['field'].queryset = Field_Education_School.objects.none()

