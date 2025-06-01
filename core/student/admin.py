from django.contrib import admin
from .models import Document_Authenticate_Student , Document_Education_Student , StudentInformation 
# Register your models here.



@admin.register(Document_Authenticate_Student)
class Document_Authenticate_Student_Admin(admin.ModelAdmin) : 
    list_display = ('student' , 'status_document_authentication')
    
    
@admin.register(Document_Education_Student)
class Document_Education_Student_Admin(admin.ModelAdmin):
    list_display = ('student' , 'status_document_education' ) 
    
@admin.register(StudentInformation)
class StudentInformation_Admin(admin.ModelAdmin):
    list_display = ('client_student' , 'phone' , 'address' ) 
    list_filter  = ('address' , ) 
    search_fields = ('client_student' , 'phone' ) 