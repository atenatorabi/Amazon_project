from django.shortcuts import render
from .models import News

# Create your views here.

def news(request):
    news_site = News.objects.all()
    return render(request , 'nesw.html', {
        'news' : news_site
    })
