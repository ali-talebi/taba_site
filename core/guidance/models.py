from django.db import models
from ckeditor.fields import  RichTextField
# Create your models here.
class RegistrationAnnouncement(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان خبر")
    content = RichTextField(verbose_name="متن خبر")
    published_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "اطلاعیه های ثبت نام"
        ordering = ['-published_at']
        