from django.contrib import admin
from .models import Contact, RestaurantAddress, Restaurant, TodaysSpecial

# registering models
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_at')
    
admin.site.register(RestaurantAddress)
admin.site.register(Restaurant)
admin.site.register(TodaysSpecial)
