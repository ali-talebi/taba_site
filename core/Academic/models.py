from django.db import models
from accounts.models import User 
from school.models import SchoolInformation , Field_Education_School , Level_Education_School 
from student.models import StudentInformation
from django.utils.translation import gettext_lazy as _


# Create your models here.


class AcademicYear(models.Model):
    name  = models.CharField(verbose_name='نام سال تحصیلی' , max_length=100 ) 
    start = models.DateField(verbose_name='شروع سال تحصیلی' ) 
    end   = models.DateField(verbose_name='پایان سال تحصیلی' ) 
    
    
    def __str__(self):
        return self.name 
    
    class Meta : 
        db_table = 'AcademicYear'
        verbose_name_plural = 'سال تحصیلی'
        
class Enrollment(models.Model):
    student = models.ForeignKey(StudentInformation, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.PROTECT)
    grade = models.ForeignKey(Level_Education_School, on_delete=models.PROTECT)
    field = models.ForeignKey(Field_Education_School, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = "تایید شده" if self.approved else "در انتظار"
        return f"{self.student} - {self.grade} ({self.academic_year}) - {status}"

# نتیجه امتحانات دانش‌آموز
class ExamResult(models.Model):
    EXAM_CHOICES = ( 
        ('KH', 'خرداد') , 
        ('SH', 'شهریور') , 
        ('DI', 'دی')
    )
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, verbose_name=_("ثبت‌نام"))
    exam_period = models.CharField(max_length=2, choices=EXAM_CHOICES , default='KH' ,  verbose_name=_("دوره امتحانی"))
    passed = models.BooleanField(verbose_name=_("آیا قبول شده؟"))
    exam_date = models.DateField(verbose_name=_("تاریخ امتحان"))

    def __str__(self):
        return f"{self.enrollment.student} - {self.get_exam_period_display()} - {'قبول' if self.passed else 'رد'}"
    
    
    class Meta : 
        db_table = 'ExamResult'
        verbose_name_plural = 'نتایج امتحان'