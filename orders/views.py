from django.shortcuts import render, redirect, get_object_or_404
from products.models import MenuItem
from .models import Order
from .serializers import OrderSerializer
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import RestrieveAPIView

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
    order_id = random.randint(1000, 9999)
    breadcrumb = [
        {'name':'Home', 'url':'/'},
        {'name':'Menu', 'url':'/menu/'},
        {'name':'Order', 'url':'/order/'},
        {'name':'Confirmation', 'url':''}
    ]
    request.session['cart'] = {}
    return render(request, 'order_confirmation.html', {'breadcrumb':breadcrumb, 'order_id':order_id})
