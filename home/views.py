import requests
import logging
import smtplib
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from .models import Feedback, Contact, RestaurantAddress, Restaurant, TodaysSpecial
from django.utils.timezone import now
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 

# configure logging
logger = logging.getLogger(__name__)

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
        restaurant = Restaurant.objects.first()

        # get cart info
        cart = request.session.get('cart',{})
        cart_item_count = sum(cart.values())

        # today special
        specials = TodaysSpecial.objects.all()

        # Home page, no additional crumbs
        breadcrumb = []
        context = {
            'restaurant_name':settings.RESTAURANT_NAME,
            'restaurant_phone': restaurant.phone if restaurant else None,
            'current_year':now().year,
            'menu_items':menu_items,
            'restaurant_address': address,
            'opening_hours':address.opening_hours if address else {},
            'query':query,
            'restaurant':restaurant,
            'breadcrumb':breadcrumb,
            'specials':specials,
            # "map_url":map_url
        }
        return render(request, 'home.html', context)
    except Exception as e:
        print(f"Error in home view : {e}")
        return HttpResponse("Oops! Something went wrong while loading the home page.", status=500)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    return redirect('home')

def user_logout(request):
    logout(request)
    return redirect('home')

def contact(request):
    """Contact view of the restaurant"""
    breadcrumb = [{'name':'Contact', 'url':request.path}]
    try:
        restaurant = Restaurant.objects.first()
        form = ContactForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                contact = form.save()

                # send email notification
                try:
                    send_mail(
                        subject=f"New contact form submission from {contact.name}",
                        message=contact.message,
                        from_email=contact.email,
                        recipient_list = [settings.RESTAURANT_EMAIL],
                        fail_silently = False,
                    )
                except smtplib.SMTPException as smtp_error:
                    logger.error(f"SMTP error while sending the email: {smtp_error})
                except Exception as mail_error:
                    logger.error(f"Email send error : {mail_error}")
                context = {
                    'restaurant':restaurant,
                    'restaurant_phone':restaurant.phone if restaurant else None,
                    'current_year':now().year,
                    'success':'Thank you for contacting us.',
                    'breadcrumb':breadcrumb,
                }
                return redirect('thank_you')
        context = {
            'form':form,
            'restaurant':restaurant,
            'restaurant_phone':restaurant.phone if restaurant else None,
            'current_year':now().year,
            'breadcrumb':breadcrumb,
        }
        return render(request, 'contact.html', context)
    except Exception as e:
        logger.exception(f"Error im contact view : {e}")
        return HttpResponse("Oops! Something went wrong while loading the contact page: {e}.",status=500)

def reservations(request):
    """Render the reservation page"""
    breadcrumb = [{'name':'Reservations', 'url': request.path}]
    return render(request, 'reservations.html', {'breadcrumb':breadcrumb})

def feedback_view(request):
    """Feedback are viewed here"""
    context = {'breadcrumb':[{'name':'Feedback', 'url':request.path}]}
    if request.method == "POST":
        name = request.POSt.get('name','').strip()
        feedback = request.POST.get('feedback', "").strip()
         
        if not name and not feedback:
            context['error'] = "Please enter both your name and feedback."
        else:
            try:
                Feedback.objects.create(name=name, feedback=feedback)
                context['success'] = "Thank you for your feedback!"
            except Exception as e:
                context['error'] = f"An error Occurred : {str(e)}"
    return render(request, "feedback.html", context)
    
def faq_view(request):
    """Rendering FAQ page"""
    breadcrumb = [{'name':'FAQ', 'url':request.path}]
    return render(request, 'faq.html', {'breadcrumb':breadcrumb})

def about_view(request):
    """Information about the restaurant"""
    breadcrumb = [{'name':'about', 'url':request.path}]
    restaurant = RestaurantAddress.objects.first()

    context = {
        'restaurant': restaurant,
        'restaurant_name': restaurant.name if restaurant else '',
        'restaurant_phone': restaurant.phone if restaurant else '',
        'restaurant_image':restaurant.image.url if restaurant and restaunrant.image else '',
        'current_year': now().year,
        'breadcrumb':breadcrumb,
    }
    return render(request, 'about.html', context)
    
