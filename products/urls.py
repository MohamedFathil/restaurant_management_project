from django.urls import path
from .views import ItemView, MenuItemView, menu_page

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('menu/', MenuItemView.as_view(), name='menu-item-list'),
    # template page
    path('menu-page/', menu_page, name='menu-page'),
]