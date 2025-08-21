from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('reservations/',views.reservations, name='reservations'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('faq/', views.faq_view, name='faq'),
]