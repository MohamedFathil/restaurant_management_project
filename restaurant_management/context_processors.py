from django.conf import settings

def restaurant_logo(request):
    return {
        "restaurant_name":getattr(settings, "RESTAURANT_NAME", "Our Restaurant"),
        "restaurant_opening_hours": getattr(settings, "RESTAURANT_OPENING_HOURS", ""),
    }