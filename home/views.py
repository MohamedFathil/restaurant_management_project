from django.shortcuts import render
from django.conf import setttings
# Create your views here.

def home(request):
    return render(request, 'home.html', {'restaurant_name':setttings.RESTAURANT_NAME})