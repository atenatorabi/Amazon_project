from django.contrib import admin
from django.urls import path
from .views import contact_us

urlpatterns =[
    path('' , contact_us , name='contactUs' )
]