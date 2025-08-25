from django.urls import path
from . import views

urlpatterns = [
    path('order/',views.order_page, name="order_page"),
    
]