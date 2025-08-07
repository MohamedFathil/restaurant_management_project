from django.shortcuts import render
from django.conf import settings
# Create your views here.

def home(request):
    context = {
        'restaurant_name':settings.RESTAURANT_NAME,
        'restaurant_phone': settings.RESTAURANT_PHONE_NUMBER
    }
    return render(request, 'home.html', context)

def contact(request):
    context = {
        'restaurant_phone':settings.RESTAURANT_PHONE
    }
    return render(request, 'contact.html', context)
