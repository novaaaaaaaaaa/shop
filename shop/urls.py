# app level urls (shop)
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('update_profile/', views.update_profile, name= "update_profile"),
    path('add_stock/', views.add_stock, name='add_stock'),
    path('display_stock/', views.display_stock, name='display_stock'),
    # path('add_to_cart/', views.add_to_cart, name='add_to_cart')
    path('add_to_shopping_list/', views.add_to_shopping_list, name='add_to_shopping_list'),
    path('shopping_list/', views.shopping_list, name='shopping_list'),
]