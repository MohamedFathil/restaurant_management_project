from django.conf import settings
from home.models from RestaurantAddress

def restaurant_info(request):
    """
    Inject restaurant details into all templates 
    """
    address = RestaurantAddress.objects.first()
    opening_hours_str = ""
    if address and address.opening_hours:
        opening_hours_str = " | ".join(
            [f"{day}:{hours}" for day, hours in address.opening_hours.items()]
        )
    return {
        "restaurant_name": address.name if address else "Our Restaurant",
        "restaurant_opening_hours": opening_hours_str,
        "restaurant_address": address.address if address else "",
        "restaurant_phone": address.phone if address else "",
        "current_year": now().year(),
    }

def breadcrumb_context(request):
    return {'breadcrumb': request.session.get('breadcrumb',[])}
