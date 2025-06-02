from django.contrib import admin
from .models import SchoolInformation , Level_Education_School , Field_Education_School
# Register your models here.


@admin.register(Field_Education_School)
class Field_Education_School_Admin(admin.ModelAdmin):
    list_display = ('field_name' , ) 
    
    


@admin.register(Level_Education_School)
class Level_Education_School_Admin(admin.ModelAdmin):
    list_display = ('name_level' , 'school' ,'Total_Fields') 
    list_filter  = ('name_level' , ) 
    
    
    def Total_Fields(self,obj):
        total_fields = ' | '.join([ i.field_name for i in obj.fields.all() ])
        return total_fields 
    Total_Fields.short_description = " رشته های تحصیلی مدرسه "

@admin.register(SchoolInformation)
class SchoolInformation_Admin(admin.ModelAdmin):
    list_display = ('school_name' , 'manager' , 'address' ) 
    list_filter  = ('address' , ) 
    search_fields = ('school_name' , )
