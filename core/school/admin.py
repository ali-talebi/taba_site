from django.contrib import admin
from .models import SchoolInformation 
# Register your models here.

@admin.register(SchoolInformation)
class SchoolInformation_Admin(admin.ModelAdmin):
    list_display = ('school_name' , 'manager' , 'address' ) 
    list_filter  = ('address' , ) 
