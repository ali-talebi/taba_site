from django.db import models
from manager.models import ManagerInformation
from MainAddress.models import Province 
# Create your models here.


class Level_Education_School(models.Model):
    school = models.OneToOneField('SchoolInformation' , verbose_name='مدرسه' , on_delete=models.CASCADE , null = True )
    name_level = models.CharField(max_length=100 , verbose_name="سطح تحصیلی مدارس" )
    
    def __str__(self):
        return self.name_level 
    
    class Meta : 
        db_table = "Level_Education_School"
        verbose_name_plural = 'سطح تحصیلی مدارس'
    


class SchoolInformation(models.Model):
    school_name = models.CharField(verbose_name="نام مدرسه" , max_length=100 ) 
    logo        = models.FileField(verbose_name="لوگوی مدرسه" , null = True , blank = True , upload_to="SchoolInformation")
    manager     = models.OneToOneField(ManagerInformation , verbose_name="مدیر مدرسه" , on_delete=models.SET_NULL , null = True )
    address     = models.ForeignKey(Province , verbose_name='آدرس' , on_delete=models.SET_NULL , null = True ) 
    
    def __str__(self) : 
        return f'{self.school_name} - {self.address} '

    class Meta : 
        db_table = 'SchoolInformation'
        verbose_name_plural = 'اطلاعات مدرسه ها'
        
        
        

    
    