from django.contrib import admin
from .models import Contact, Restaurant

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_at')
    
admin.site.register(Restaurant)
