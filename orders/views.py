from django.shortcuts import render

def order_page(request):
    breadcrumb = [
        {'name':'Home', 'url':'/'},
        {'name':'Order', 'url':'/order/'}
    ]
    return render(request, 'order.html',{'breadcrumb':breadcrumb})
