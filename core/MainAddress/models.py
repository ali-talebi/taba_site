from django.db import models

# Create your models here.

class Country(models.Model):
    name_country = models.CharField(verbose_name='نام کشور' , max_length=20)
    def __str__(self):
        return self.name_country 
    class Meta : 
        db_table = 'Country'
        verbose_name_plural = 'کشورها'
        
        
class Province(models.Model):
    country = models.ForeignKey(Country,verbose_name='کشور' , on_delete=models.CASCADE )
    name_province = models.CharField(verbose_name='نام استان' , max_length=20 )
    
    def __str__(self):
        return f'{self.country} - {self.name_province} ' 
    
    class Meta : 
        db_table = "Province"
        verbose_name_plural = 'استان ها'
        