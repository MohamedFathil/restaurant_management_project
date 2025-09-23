from rest_framework import serializers
from .models import Order
from products.models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','name','price']

class OrderSerializer(serializers.ModelSerializer):
    order_items = MenuItemSerializer(many=True, read_only=True)
    customer = serializers.StringRelatedField()
    status = serializers.StringRelatedField()
    class Meta:
        model = Order
        fields = ['id','customer','created_at','total_amount', 'order_items', 'order_status']

class OrderCancelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','status']

        def update(self, instance, validated_data):
            instance.status = 'cancelled'
            instance.save()
            return instance

