from django.conf import settings
from account.models from RestaurantAddress

def restaurant_info(request):
    return {
        "restaurant_name":getattr(settings, "RESTAURANT_NAME", "Our Restaurant"),
        "restaurant_opening_hours": getattr(settings, "RESTAURANT_OPENING_HOURS", ""),
    }