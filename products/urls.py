from django.urls import path
from .views import ItemView, MenuItemView, menu_page, MenuCategoryView, MenuItemByCategoryView, MenuItemUpdateView  

urlpatterns = [
    path('api/items/', ItemView.as_view(), name='item-api'),
    path('api/menu/', MenuItemView.as_view(), name='menu-api'),
    path('api/menu-categories/', MenuCategoryView.as_view(), name='menu-categories'),
    path('api/items-by-category/',MenuItemByCategoryView.as_view(), name='items_by_category'),
    path('menu/update/<int:pk>/', MenuItemUpdateView.as_view(), name='menuitem-update'),
    # template page
    path('menu-page/', menu_page, name='menu-page'),
]