from django.shortcuts import render ,redirect
from .models import Product_List , ProductCategory , Product_color
# Create your views here.
new_pro = None
def product_list(request):
    products = Product_List.objects.filter(is_active=True).order_by('price')
    new_products = products.order_by('-id')[:3]
    global new_pro
    new_pro = new_products
    return render(request , 'product-list.html' , {
        'products' : products,
        'new_pro' : new_products,

    })


def product_details(request ,slug):
    product = Product_List.objects.filter(slug=slug).first()
    if new_pro is None:
        return redirect('product_list')
    colors = Product_color.objects.filter(product_list=product)
    return render(request , 'product-details.html' , {
        'product' : product,
        'new_pro' :new_pro,
        'colors' : colors,


    })


def product_categories(request , id):
    category = ProductCategory.objects.filter(id=id).first()
    products = Product_List.objects.filter(category=category)
    return render(request , 'product-list.html' , {
        'products': products,

    })





