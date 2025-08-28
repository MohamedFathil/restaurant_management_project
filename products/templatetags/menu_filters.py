from django import template

register = template.Library()

@register.filter(name='availability_status')
def availability_status(is_available):
    """
    Return 'Available' if True, else 'Coming Soon'
    """
    return 'Avilable' if is_available else 'Coming Soon'