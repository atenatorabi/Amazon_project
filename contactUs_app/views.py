from django.shortcuts import render

from .models import ContactUsModel


# Create your views here.


def contact_us(request):
    if request.method == 'GET':
        return render(request, 'contact_us_page.html', {
        })
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        new_message = ContactUsModel(full_name=name, email=email, subject=subject, message=message)
        new_message.save()
        return render(request, 'contact_us_page.html', {
            'result' : True
        })
