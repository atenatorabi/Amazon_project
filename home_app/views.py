

import requests
from django.shortcuts import render
from product_app.models import ProductCategory


# Create your views here.

def home_page(request):
    return render(request , 'home-page.html' ,{

    })



def header_component(request):
    categories = ProductCategory.objects.filter(is_active=True)
    resualt = requests.get("https://BrsApi.ir/Api/Market/Gold_Currency.php?key=FreeBiEfay2EoIUnz6cwIxhiSIaPoFnA")
    data = resualt.json()
    price = data['currency'][1]['price']
    print(data)
    return render(request , 'header.html' ,{
        'important_news' : f'اخرین قیمت دلار{price}تومان ' ,
        'categories' : categories

    })


def footer_component(request):
    return render(request, 'footer.html', {

    })