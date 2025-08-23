from django.shortcuts import render
import random

def order_page(request):
    breadcrumb = [
        {'name':'Home', 'url':'/'},
        {'name':'Order', 'url':'/order/'}
    ]
    return render(request, 'order.html',{'breadcrumb':breadcrumb})

def order_confirmation(request):
    order_id = random.randint(1000, 9999)
    breadcrumb = [
        {'name':'Home', 'url':'/'},
        {'name':'Menu', 'url':'/menu/'},
        {'name':'Order', 'url':'/order/'},
        {'name':'Confirmation', 'url':''}
    ]
    return render(request, 'order_confirmation.html', {'breadcrumb':breadcrumb, 'order_id':order_id})
