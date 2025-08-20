from django.contrib import admin
from .models import MenuItem

# Custom Admin
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name','description','price','created_at']
    search_field = ['name']
