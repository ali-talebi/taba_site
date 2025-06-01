from django.contrib import admin
from .models import ManagerInformation , DocumentManager 
# Register your models here.



@admin.register(ManagerInformation)
class ManagerInformation_Admin(admin.ModelAdmin):
    list_display  = ('client_manager' , 'phone_number1' , 'address' ) 
    list_filter   = ('address' ,  )
    search_fields = ('client_manager' , )
    
@admin.register(DocumentManager)
class DocumentManager_Admin(admin.ModelAdmin):
    list_display = ('manager' ,  ) 
    
    
    
    