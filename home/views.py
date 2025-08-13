from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .models import Feedback

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

def feedback_view(request):
    """Feedback are viewed here"""
    if request.method == "POST":
        comment = request.POST.get('comment', "").strip()
        return render(request, 'feedback.html', {"error":"Please enter a comment"})
    
    try:
        Feedback.objects.create(comment=comment)
        return render(request, 'feedback.html', {"success":"Thank you for your feedback"})
    except Exception as e:
        return render(request, "feedback.html",{"error":f"An error occured: str(e)"})
    return render(request, "feedback.html")