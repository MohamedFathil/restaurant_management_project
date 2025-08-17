from django.contrib import admin
from .models import Contact, RestaurantAddress

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_at')
    
admin.site.register(RestaurantAddress)
