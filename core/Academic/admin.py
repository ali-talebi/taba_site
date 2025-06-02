from django.contrib import admin
from .models import AcademicYear , Enrollment , ExamResult 
# Register your models here.


@admin.register(AcademicYear)
class AcademicYear_Admin(admin.ModelAdmin):
    list_display = ('name','start','end')
    
@admin.register(Enrollment)
class Enrollment_Admin(admin.ModelAdmin):
    list_display = ('student' ,'academic_year' , 'grade' , 'field' , 'approved')
    list_filter  = ('student' ,'academic_year' , 'grade' , 'field' , 'approved')
    
@admin.register(ExamResult)
class ExamResult_Admin(admin.ModelAdmin):
    list_display = ('enrollment' , 'exam_period','passed')
    list_filter  = ('enrollment' , 'exam_period','passed')