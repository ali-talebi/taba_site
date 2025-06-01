from django.db import models
from accounts.models import User 
from MainAddress.models import Country , Province 
# Create your models here.


class DocumentManager(models.Model):
    manager = models.OneToOneField('ManagerInformation',on_delete=models.CASCADE )
    doc1 = models.FileField(upload_to="DocumentManager/" , verbose_name='سند 1 احراز هویت کاربری ' )
    doc2 = models.FileField(upload_to="DocumentManager/" , verbose_name='سند 2 احراز هویت کاربری ' )
    doc3 = models.FileField(upload_to="DocumentManager/" , verbose_name='سند 3 احراز هویت کاربری ' )
    doc4 = models.FileField(upload_to="DocumentManager/" , verbose_name='سند 4 احراز هویت کاربری ' )
    
    def __str__(self):
        return f'{self.manager} - {self.manager.client_manager.email}' 
    
    class Meta : 
        db_table = 'DocumentManager'
        verbose_name_plural = 'سند احراز هویت مدیران'
    

class ManagerInformation(models.Model):
    client_manager = models.OneToOneField(User,verbose_name='کاربر' , on_delete=models.CASCADE  )
    phone_number1  = models.CharField(verbose_name='شماره تماس' , max_length=11 ) 
    phone_number2  = models.CharField(verbose_name='شماره تماس' , max_length=11 , null=True , blank=True )
    address        = models.ForeignKey(Province , verbose_name='آدرس' , on_delete=models.SET_NULL , null = True )
    address2       = models.TextField(verbose_name='جزئیات منزل' )
    
    def __str__(self):
        return self.client_manager.email
    class Meta:
        db_table = 'ManagerInformation'
        verbose_name_plural = 'مشخصات مدیران'
     
    