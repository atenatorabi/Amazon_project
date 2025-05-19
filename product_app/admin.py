from django.contrib import admin
from .models import Product_List , ProductCategory , Product_color
# Register your models here.

admin.site.register(Product_List)
admin.site.register(ProductCategory)
admin.site.register(Product_color)