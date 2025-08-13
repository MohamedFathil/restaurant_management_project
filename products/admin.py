from django.contrib import admin
from .models import Order


# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']
    search_field = ['item_name']

# Register your models here.
admin.site.register(MenuItem,MenuItemAdmin)