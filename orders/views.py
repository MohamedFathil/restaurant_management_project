from django.shortcuts import render, redirect
import random


def add_to_cart(request, product_id):
    cart = request.session.get('cart',{})
    cart[item_id] = cart.get(item_id, 0) + 1
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
    return render(request, 'order_confirmation.html', {'breadcrumb':breadcrumb, 'order_id':order_id})
