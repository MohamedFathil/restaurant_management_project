import os
import django

# setup django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_management.settings')
django.setup()

from django.conf import settings
from home.models import *
from products.models import *
from orders.models import *

def greet_user(name):
    """
    Greet the user by name
    """
    return f"Hello {name}! Welcome to {settings.RESTAURANT_NAME}."

def get_contact_info():
    """
    Retrieves restaurant contact info from settings or database
    """
    try:
        phone = getattr(settings, 'RESTAURANT_PHONE', None)
        email = getattr(settings, 'RESTAURANT_EMAIL', None)
        if not phone or not email:
            raise ValueError("Contact info missing in settings.")
        return {
            'phone':phone,
            'email':email
        }
    except Exception as e:
        print("Error fetching contact info: ",e)
        return {
            'phone':'Not Available',
            'email':'Not Available'
        }

def show_menu():
    """
    Displays all available products from the database
    """
    from products.models import Products
    try:
        products = Products.objects.all()
        if not products:
            print("No products available")
            return 
        print("\nMenu : ")
        for product in products:
            print(f" - {product.name}: {product.price}")
    except Exception as e:
        print("Error", e)

def main():
    """
    Main logic function to simulate a basic run of system
    """
    print("="*40)
    print(greet_user("John"))

    #Display contact
    contact_info = get_contact_info()
    print('\n Contact Info:')
    print(f"Phone : {contact_info['phone']}")
    print(f"Email : {contact_info['email']}")

    # show menu
    show_menu()
    print("="*40)

if __name__ == '__main__':
    main()