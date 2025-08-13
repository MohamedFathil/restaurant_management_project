from django.contrib import admin
from .models import MenuItem


# Custom Admins
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']
    search_field = ['item_name']

# Register your models here.
admin.site.register(MenuItem,MenuItemAdmin)