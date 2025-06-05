from django.contrib import admin
from .models import TicketInformation 
# Register your models here.



@admin.register(TicketInformation)
class TicketInformation_Admin(admin.ModelAdmin):
    list_display = ('client_ticket' , 'title' , 'status' , 'user_type' ) 
    list_filter  = ('client_ticket' , 'status' , 'user_type')  
    search_fields = ('client_ticket' , )