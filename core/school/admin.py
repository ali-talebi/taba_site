from django.contrib import admin
from .models import SchoolInformation , Level_Education_School , Field_Education_School
# Register your models here.


@admin.register(Field_Education_School)
class Field_Education_School_Admin(admin.ModelAdmin):
    list_display = ('field_name' , ) 
    
    


@admin.register(Level_Education_School)
class LevelEducationAdmin(admin.ModelAdmin):
    list_display = ['school', 'name_level', 'get_education_fields']

    def get_education_fields(self, obj):
        return ", ".join([field.field_name for field in obj.education_fields.all()])
    
    get_education_fields.short_description = "رشته‌های تحصیلی"
    


@admin.register(SchoolInformation)
class SchoolInformation_Admin(admin.ModelAdmin):
    list_display = ('school_name' , 'manager' , 'address' ) 
    list_filter  = ('address' , ) 
    search_fields = ('school_name' , )
