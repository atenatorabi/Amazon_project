from django.db import models

# Create your models here.

class ContactUsModel(models.Model):
    full_name = models.CharField(max_length=100 , verbose_name='نام کامل')
    email = models.EmailField(max_length=200 , verbose_name='ادرس ایمیل')
    subject = models.CharField(max_length=300 , verbose_name='موضوع')
    message = models.TextField(verbose_name='متن پیام')
    is_read_by_admin = models.BooleanField(default=False , verbose_name='خوانده شده')
    response = models.TextField(verbose_name='پاسخ پیام' , null=True , blank=True)
    def __str__(self):
        return f'{self.email} - {self.subject}'

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'
