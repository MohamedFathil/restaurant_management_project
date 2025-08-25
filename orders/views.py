from django.shortcuts import render, redirect
import random


def add_to_cart(request, item_id):
    """Add item to the cart"""
    cart = request.session.get('cart',{})
    cart[item_id] = cart.get(item_id, 0) + 1
    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    """View cart page"""
    cart = request.session.get('cart',{})
    breadcrumb = [
        {'name':'Home','url':'/'},
        {'name':'Cart', 'url':'/cart/'}
    ]
    return render(request, 'cart.html', {'breadcrumb':breadcrumb, 'cart':cart})

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
