from django.contrib import admin
from .models import RegistrationAnnouncement 
# Register your models here.


@admin.register(RegistrationAnnouncement)
class RegistrationAnnouncement_Admin(admin.ModelAdmin):
    list_display = ('title' , 'is_active')