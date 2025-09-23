import secrets
import string
from .models import Coupon, Order
import logging
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

def generate_coupon_code(length=10):
    """Generates coupon code"""
    characters = string.ascii_uppercase + string.digits

    while True:
        code = ''.join(secrets.choice(characters) for _ in range(length))

        if not Coupon.objects.filter(code=code).exists():
            return code

logger = logging.getLogger(__name__)

def send_order_confirmation_email(order_id, customer_email, customer_name, total_amount, coupon_code=None):
    """
    Send Order confirmation email to the customer
    """
    try:
        subject = f"Order Confirmation : Order ${order_id}\n\n"
        message = f"Hi {customer_name},\n"
        message += f"Thank you for your order #{order_id}.\n"
        message += f"Total Amount : Rs{total_amount}\n"
        if coupon_code:
            message += f"Here's a special coupon for you: {coupon_code}\n"
        message += "\nWe hope to see you again soon!\n\nBest Regards,\nReaturant Team"
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email],
            fail_silently=False
        )
        return "Email sent successfully"
    except Exception as e:
        return f"Failed to sent : {str(e)}"

def generate_unique_order_id(length=8):
    """
    Generate unique alphanumeric order ID.
    """
    characters = string.ascii_uppercase + string.digits

    while True:
        order_id = ''.join(secrets.choice(characters)) for _ in range(length)
        if not Order.objects.filter(unique_id=order_id).exists():
            return order_id
