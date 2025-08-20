from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('reservations/',views.reservations, name='reservations'),
    path('contact/', views.contact_view, name='contact'),
    path('feedback/', views.feedback_view, name='feedback'),
]