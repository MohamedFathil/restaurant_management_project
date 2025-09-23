from django.core.mail import send_mail, BadHeaderError
import logging
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.conf import settings

logger = logging.getLogger(__name__)

def send_app_email(recipient_email: str, subject: str, message: str) -> bool:
    try:
        validate_email(recipient_email)

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email],
            fail_silently=False,
        )
        logger.info(f"Email sent successfully to {recipient_email}")
        return True
    except ValidationError:
        logger.warning("Invalid email address")
        return False
    except BadHeaderError:
        logger.error("Invalid header found when sending email")
        return False
    except Exception as e:
        logger.error(f"Unexpected error sending email to {recipient_email}: {str(e)}" )
        return False
