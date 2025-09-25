from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reservations/',views.reservations, name='reservations'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('faq/', views.faq_view, name='faq'),
    path('about/', views.about_view, name='about'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('thank-you/', TemplateView.as_view(template_name='thank_you.html'), name='thank_you'),
    path('about-chef/', views.about_chef, name='about_chef'),
    path('newsletter-signup/',views.newsletter_signup, name='newsletter_signup'),
    path('our-story/', views.our_story, name="our_story"),
    path('our-team/', views.our_team, name="our_team"),
    path('gallery/', views.gallery, name="gallery"),
    path('location/', views.location, name="location"),
    path('api/contact/', views.ContactFormSubmissionView.as_view(), name='contact-form'),
    path('daily-special/', views.DailySpecialsView.as_view(), name='daily-specials')
]
