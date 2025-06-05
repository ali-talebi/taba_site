from django.db import models
from accounts.models import User 
# Create your models here.


class TicketInformation(models.Model):
    status_level = (
        ('no_check', 'در انتظار بررسی'),
        ('checking', 'در حال بررسی'),
        ('answered', 'پاسخ داده شده'),
    )
    client_ticket = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر تیکت')
    title = models.CharField(verbose_name='عنوان پیام', max_length=100)
    text = models.TextField(verbose_name='متن پیام')
    status = models.CharField(verbose_name='وضعیت تیکت', choices=status_level, default='no_check', max_length=12)
    user_type = models.CharField(max_length=10, choices=(('manager', 'مدیر'), ('student', 'دانش‌آموز')), default='student')

    # 🆕 پاسخ ادمین
    reply = models.TextField(verbose_name='پاسخ مدیر/ادمین', blank=True, null=True)

    def __str__(self):
        return f'{self.client_ticket.email} - {self.title}'

    class Meta:
        db_table = 'TicketInformation'
        verbose_name_plural = 'تیکت‌های دریافتی'
        