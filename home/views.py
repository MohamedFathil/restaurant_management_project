from django.shortcuts import render
from django.conf import settings
# Create your views here.

def home(request):
    context = {
        'restaurant_name':settings.RESTAURANT_NAME
    }
    return render(request, 'home.html', context)