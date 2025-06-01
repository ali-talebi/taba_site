from django.contrib import admin
from .models import Country , Province 
# Register your models here.



@admin.register(Country)
class Country_Admin(admin.ModelAdmin):
    list_display = ('name_country' , ) 
    list_filter  = ('name_country' , ) 
    
@admin.register(Province)
class Province_Admin(admin.ModelAdmin):
    list_display = ('name_province' , 'country') 
    list_filter  = ('country' , ) 
    

    
    