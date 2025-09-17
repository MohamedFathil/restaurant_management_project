import logging
from django.core.validators import valid_email
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

def is_valid_email(email: str) -> bool:
    """
    Validate an email address using Django's built-in validator.
    Returns True if valid, False otherwise
    """
    try:
        valid_email(email)
        return True
    except ValidationError:
        logger.warning(f"Invalid email attempted: {email}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error validating email {email}: {str(e)}")
        return False
