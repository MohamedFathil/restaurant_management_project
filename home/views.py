import requests
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from .models import Feedback, Contact, RestaurantAddress
from django.utils.timezone import now
from django.core.mail import send_mail
from .forms import ContactForm

def home(request):
    try:
        # Fetch menu data from API
        api_url = f"{settings.SITE_URL}/api/menu"
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        menu_items = response.json()
        # handle search
        query = request.GET.get("q","").strip()
        if query:
            menu_items = [
                item for item in menu_items
                if query.lower() in item['name'].lower()
            ]

        address = RestaurantAddress.objects.first()
        context = {
            'restaurant_name':settings.RESTAURANT_NAME,
            'restaurant_phone': settings.RESTAURANT_PHONE_NUMBER,
            'current_year':now().year,
            'menu_items':menu_items,
            'restaurant_address': address,
            'opening_hours':address.opening_hours if address else {},
            'query':query,  
            # "map_url":map_url
        }
        return render(request, 'home.html', context)
    except Exception as e:
        print(f"Error in home view : {e}")
        return HttpResponse("Oops! Something went wrong while loading the home page.", status=500)

def contact(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name','').strip()
            email = request.POST.get('email','').strip()
            message = request.POST.get('message','').strip()
            if not name or not email or not message:
                context = {
                    'restaurant_phone':settings.RESTAURANT_PHONE_NUMBER,
                    'current_year':now().year,
                    'error':'Please fill out all fields.'
                }
                return render(request, 'contact.html', context)
                
            # contact entry
            Contact.objects.create(name=name, email=email, message=message)

            # send email notification
            try:
                send_mail(
                    subject=f"New contact form submission from {name}",
                    message=message,
                    from_email=email,
                    recipient_list = [settings.RESTAURANT_EMAIL],
                    fail_silently = False,
                )
            except Exception as mail_error:
                print(f"Email send error : {mail_error}")
            context = {
                'restaurant_phone':settings.RESTAURANT_PHONE_NUMBER,
                'current_year':now().year,
                'success':'Thank you for contacting us.'
            }
            return render(request, 'contact.html', context)
        context = {
            'restaurant_phone':settings.RESTAURANT_PHONE_NUMBER,
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
        return render(request, "feedback.html",{"error":f"An error occured: {str(e)}"})
    return render(request, "feedback.html")

