from django.shortcuts import render, redirect, get_object_or_404
from products.models import MenuItem
from .models import Order, Coupon
from .serializers import OrderSerializer
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import RestrieveAPIView
from .utils import generate_coupon_code, send_order_confirmation_email
from datetime import timedelta
from django.utils import timezone

class OrderHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            orders = Order.objects.filter(customer=request.user).order_by('-created_at')
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error':'Unable to fetch order history', 'detail':str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class OrderDetailView(RestrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

def add_to_cart(request, item_id):
    """Add item to the cart"""
    item = get_object_or_404(MenuItem, id=item_id)
    cart = request.session.get('cart',{})
    if str(item_id) in cart:
        cart[str(item_id)]['quantity'] += 1
    else:
        cart[str(item_id)] = {
            'name':item.name,
            'price': float(item.price),
            'quantity':1
        }
    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    """View cart page"""
    cart = request.session.get('cart',{})
    total_price = sum(item['price']* item['quantity'] for item in cart.values())
    breadcrumb = [
        {'name':'Home','url':'/'},
        {'name':'Cart', 'url':'/cart/'}
    ]
    return render(request, 'cart.html', {'breadcrumb':breadcrumb, 'cart':cart, 'total_price':total_price})

def remove_from_cart(request, item_id):
    """Remove item from the cart"""
    cart = request.session.get('cart',{})
    item_id = str(item_id)
    if item_id in cart:
        del cart[item_id]
    request.session['cart'] = cart
    return redirect('view_cart')

def order_confirmation(request):
    order_id = 1243
    coupon_code = generate_coupon_code()
    coupon = Coupon.objects.create(
        code=coupon_code,
        discount = 10,
        valid_from = timezone.now(),
        valid_to = timezone.now() + timedelta(days=7),
        active = True
    )
    customer_email = request.user.email
    customer_name = request.user.get_full_name() or request.user.username
    total_amount = 450.0

    email_status = send_order_confirmation_email(order_id, customer_email, customer_name, total_amount, coupon_code)
    print(email_status)
    breadcrumb = [
        {'name':'Home', 'url':'/'},
        {'name':'Menu', 'url':'/menu/'},
        {'name':'Order', 'url':'/order/'},
        {'name':'Confirmation', 'url':''}
    ]
    request.session['cart'] = {}
    # pass coupon details
    return render(request, 'order_confirmation.html', {'breadcrumb':breadcrumb, 'order_id':order_id,'coupon':coupon})

class CancelOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id, customer=request.user)
        except Order.DoesNotExist:
            return Response(
                {'error':"Order does not exist"},
                status = status.HTTP_404_NOT_FOUND
            )
        if order.status.name.lower() in ['completed','cancelled']:
            return Response(
                {"error":"This order cannot be cancelled"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        order.status.name = 'cancelled'
        order.status.save()
        return Response(
            {"message": f"Order {order.id} has been cancelled"},
            status=status.HTTP_200_OK
        )

class UpdateOrderStatusView(APIView):
    def post(self, request, *args, **kwargs):
        order_id = request.data.get("order_id")
        new_status = request.data.get("status")

        if not order_id or not new_status:
            return Response(
                {"error":"order_id and status are required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        order = get_object_or_404(Order, id=order_id)

        allowed_status = dict(Order.STATUS_CHOICES).key()
        if new_status not in allowed_status:
            return Response(
                {"error":"Invalid status"},
                status=status.HTTP_400_BAD_REQUEST
            )

        order.status = new_status
        order.save()

        return Response(
            {"message":f"Order {order.id} status updated"},
            status=status.HTTP_200_OK
        )