from django.contrib import admin
from .models import News
# Register your models here.
class ImportandNewsAdmin(admin.ModelAdmin):
    List_display = ['news_name' , 'user' , 'images']
admin.site.register(News , ImportandNewsAdmin)