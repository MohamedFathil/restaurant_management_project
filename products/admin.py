from django.contrib import admin
from .models import MenuItem


# Custom Admins
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name','description','price','created_at']
    search_field = ['name']

# Register your models here.
admin.site.register(MenuItem,MenuItemAdmin)