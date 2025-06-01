from django.db import models
from accounts.models import User 
from MainAddress.models import Province 
# Create your models here.

class Document_Education_Student(models.Model):
    
    STATUS_CHOICES = ( 
    ('no_check' , 'no_check' ) ,
    ('approved' , 'approved' ) , 
    ('failed','failed') )
    
    student = models.OneToOneField('StudentInformation' ,verbose_name='دانش آموز',on_delete=models.CASCADE)
    file1   = models.FileField(verbose_name='مدرک تحصیلی پایه 1 ' , upload_to="Document_Education_Student" , null=True , blank = True ) 
    file2   = models.FileField(verbose_name='مدرک تحصیلی پایه 2 ' , upload_to="Document_Education_Student" , null=True , blank = True ) 
    file3   = models.FileField(verbose_name='مدرک تحصیلی پایه 3 ' , upload_to="Document_Education_Student" , null=True , blank = True ) 
    file4   = models.FileField(verbose_name='مدرک تحصیلی پایه 4 ' , upload_to="Document_Education_Student" , null=True , blank = True ) 
    file5   = models.FileField(verbose_name='مدرک تحصیلی پایه 5 ' , upload_to="Document_Education_Student" , null=True , blank = True ) 
    file6   = models.FileField(verbose_name='مدرک تحصیلی پایه 6 ' , upload_to="Document_Education_Student" , null=True , blank = True ) 
    file7   = models.FileField(verbose_name='مدرک تحصیلی پایه 7 ' , upload_to="Document_Education_Student" , null=True , blank = True ) 
    file8   = models.FileField(verbose_name='مدرک تحصیلی پایه 8 ' , upload_to="Document_Education_Student" , null=True , blank = True ) 
    file9   = models.FileField(verbose_name='9 ' , upload_to="Document_Education_Student" , null=True , blank = True ) 
    file10   = models.FileField(verbose_name='مدرک تحصیلی پایه 10 ' , upload_to="Document_Education_Student" , null=True , blank = True ) 
    file11   = models.FileField(verbose_name='مدرک تحصیلی پایه 11 ' , upload_to="Document_Education_Student" , null=True , blank = True ) 
    file12   = models.FileField(verbose_name='12 ' , upload_to="Document_Education_Student" , null=True , blank = True ) 
    status_document_education = models.CharField(max_length=15 ,verbose_name='وضعیت مدارک تحصیلی' , choices=STATUS_CHOICES , default='no_check')

    def __str__(self):
        return self.student.client_student.email  

    class Meta : 
        db_table = 'Document_Education_Student'
        verbose_name_plural = 'مدارک تحصیلی دانش آموزان'

class Document_Authenticate_Student(models.Model) : 
    
    STATUS_CHOICES = ( 
    ('no_check' , 'no_check' ) ,
    ('approved' , 'approved' ) , 
    ('failed','failed') )
    
    student = models.OneToOneField('StudentInformation' ,verbose_name='دانش آموز',on_delete=models.CASCADE)
    doc1    = models.FileField(verbose_name='مدرک هویتی 1 ' , upload_to="DocumentStudent" )
    doc2    = models.FileField(verbose_name='مدرک هویتی 2 ' , upload_to="DocumentStudent" )
    doc3    = models.FileField(verbose_name='مدرک هویتی 3 ' , upload_to="DocumentStudent" )
    status_document_authentication = models.CharField(verbose_name='وضعیت مدارک هویتی' ,max_length=15 , choices=STATUS_CHOICES , default='no_check' , null = True  ) 
    
    def __str__(self):
        return self.student.email 
    
    class Meta : 
        db_table = 'Document_Authenticate_Student'
        verbose_name_plural = "مدارک هویتی دانش آموزان"



class StudentInformation(models.Model):
    STATUS_CHOICES = ( 
    ('no_check' , 'no_check' ) ,
    ('approved' , 'approved' ) , 
    ('failed','failed') )
    client_student = models.OneToOneField(User,verbose_name="دانش آموز" , on_delete=models.CASCADE ) 
    phone = models.CharField(verbose_name='شماره تماس' , max_length=11 , null = True , blank = True ) 
    address = models.ForeignKey(Province,verbose_name='آدرس' , on_delete=models.SET_NULL , null = True )
    status  = models.CharField(verbose_name="وضعیت  احراز هویت " , max_length=15 , choices=STATUS_CHOICES , default='no_check')
    
    def __str__(self):
        return self.client_student.email
    
    
    
    
    class Meta : 
        db_table = 'StudentInformation'
        verbose_name_plural = 'اطلاعات هویتی دانش آموزان'
        

     
    
