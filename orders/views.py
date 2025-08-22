from django.shortcuts import render

def order_page(request):
    breadcrumb = [
        {'name':'Home', 'url':'/'},
        {'name':'Order', 'url':'/order/'}
    ]
    return render(request, 'order.html',{'breadcrumb':breadcrumb})

def order_confirmation(request):
    breadcrumb = [
        {'name':'Home', 'url':'/'},
        {'name':'Menu', 'url':'/menu/'},
        {'name':'Order', 'url':'/order/'},
        {'name':'Confirmation', 'url':''}
    ]
    return render(request, 'order_confirmation.html', {'breadcrumb':breadcrumb})
