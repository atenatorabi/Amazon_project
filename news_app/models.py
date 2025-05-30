from django.db import models


# Create your models here.
class News(models.Model):
    news_name = models.CharField(max_length=200 , verbose_name= 'نام خبر' , default='خبر بدون عنوان')
    user = models.CharField(max_length=200, verbose_name='نام کاربر')
    date = models.DateField(auto_now_add=True, verbose_name='تاریح انتشار')
    time = models.TimeField(auto_now_add=True, verbose_name='ساعت انتشار')
    news = models.CharField(max_length=400, verbose_name='اخبار ما')

    def __str__(self):
        return f"{self.news_name} , {self.user}"

    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'
