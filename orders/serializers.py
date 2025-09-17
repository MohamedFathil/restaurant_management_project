from rest_framework import serializers
from .models import Order
from products.order import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','name','price']

class OrderSerializer(serializers.ModelSerializer):
    order_items = MenuItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id','created_at','total_amount', 'order_items', 'order_status']
