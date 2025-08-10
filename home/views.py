from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

def home(request):
    try:
        context = {
            'restaurant_name':settings.RESTAURANT_NAME,
            'restaurant_phone': settings.RESTAURANT_PHONE_NUMBER,
            'current_year':now().year
        }
        return render(request, 'home.html', context)
    except Exception as e:
        print(f"Error in home view : {e}")
        return HttpResponse("Oops! Something went wrong while loading the home page.", status=500)

def contact(request):
    try:
        context = {
            'restaurant_phone':settings.RESTAURANT_PHONE,
            'current_year':now().year
        }
        return render(request, 'contact.html', context)
    except Exception as e:
        print(f"Error im contact view : {e}")
        return HttpResponse("Oops! Something went wrong while loading the contact page.",status=500)

def reservations(request):
    """Render the reservation page"""
    return render(request, 'reservations.html')