from django.contrib import admin
from .models import Product_List , ProductCategory , Product_color
from django.contrib import admin



class ProductListAdmin(admin.ModelAdmin):
    list_display = ['title', 'price' , 'image']

# Register your models here.

admin.site.register(Product_List , ProductListAdmin)
admin.site.register(ProductCategory)
admin.site.register(Product_color)