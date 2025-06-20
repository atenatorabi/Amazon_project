"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path , include
import contactUs_app.urls

import contactUs_app
from home_app.views import home_page
from product_app.views import *
from news_app.views import news
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home_page , name='home' ),
    path('products/' , product_list , name='products-list'),
    path('details/<slug>/' , product_details , name='product-details'),
    path('category/<id>/' , product_categories , name='category'),
    path('news/' , news , name='news'),
    path('contactus/', include(contactUs_app.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)