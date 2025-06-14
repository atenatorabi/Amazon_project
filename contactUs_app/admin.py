from django.contrib import admin

from .models import ContactUsModel


# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['full_name' , 'email' , 'subject' , 'is_read_by_admin']
    list_filter = ['is_read_by_admin']



admin.site.register(ContactUsModel,ContactUsAdmin)
