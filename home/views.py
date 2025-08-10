from django.shortcuts import render
from django.conf import settings

def home(request):
    context = {
        'restaurant_name':settings.RESTAURANT_NAME,
        'restaurant_phone': settings.RESTAURANT_PHONE_NUMBER,
        'current_year':now().year
    }
    return render(request, 'home.html', context)

def contact(request):
    context = {
        'restaurant_phone':settings.RESTAURANT_PHONE,
        'current_year':now().year
    }
    return render(request, 'contact.html', context)

def reservations(request):
    """Render the reservation page"""
    return render(request, 'reservations.html')