from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','total_amount','order_status','created_at']
    list_filter = ['order_status','created_at']
    search_field = ['customer__username']
    filter_horizontal = ('order_items',)

admin.site.register(Order, OrderAdmin)

