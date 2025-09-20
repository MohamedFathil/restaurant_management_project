import secrets
import string
from .models import Coupon
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

def send_order_confirmation_email(order_id, customer_email, customer_name, total_amount):
    """
    Send Order confirmation email to the customer
    """
    subject = f"Order Confirmation : Order ${order_id}"
    message = (
        f"Hello {customer_name},\n\n",
        f"Thank you for your order!\n",
        f"Your order ID is {order_id}\n",
        f"Total amount : Rs{total_amount}\n\n",
        f"We will notify you once your order is  processed.\n\n",
        "Best Regards,\n"
        "Restaurant Team"
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    try:
        send_mail(subject, message, from_email, [customer_email], fail_silently=False)
        return {"success":True, "message":"Mail Sent"}
    except BadHeaderError:
        logger.error(f"Invalid header fount")
        return {"success":False, "message":"Invalid header"}
    except Exception as e:
        logger.error("Failed to sent mail")
        return {"succes":False, "message":str(e)}
        

