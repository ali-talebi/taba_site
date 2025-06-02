from django.contrib import admin
from .models import SchoolInformation , Level_Education_School
# Register your models here.


@admin.register(Level_Education_School)
class Level_Education_School_Admin(admin.ModelAdmin):
    list_display = ('name_level' , 'school' ) 
    list_filter  = ('name_level' , ) 
    
    

@admin.register(SchoolInformation)
class SchoolInformation_Admin(admin.ModelAdmin):
    list_display = ('school_name' , 'manager' , 'address' ) 
    list_filter  = ('address' , ) 
    search_fields = ('school_name' , )
