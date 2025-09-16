from django.urls import path
from .views import ItemView, MenuItemView, menu_page, MenuCategoryView

urlpatterns = [
    path('api/items/', ItemView.as_view(), name='item-api'),
    path('api/menu/', MenuItemView.as_view(), name='menu-api'),
    path('api/menu-categories/', MenuCategoryView.as_view(), name='menu-categories'),
    # template page
    path('menu-page/', menu_page, name='menu-page'),
]