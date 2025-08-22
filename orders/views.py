from django.shortcuts import render

def order_page(request):
    return render(request, 'order.html')
