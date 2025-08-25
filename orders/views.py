from django.shortcuts import render, redirect, get_object_or_404
from products.models import MenuItem
import random


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
    return render(request, 'cart.html', {'breadcrumb':breadcrumb, 'cart':cart. 'total_price':total_price})

def remove_from_cart(request, item_id):
    """Remove item from the cart"""
    cart = request.session.get('cart',{})
    if item_id in cart:
        def cart[item_id]
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
