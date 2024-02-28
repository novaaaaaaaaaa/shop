# app level urls (customers)
from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('login_customer', views.login_customer, name='login_customer'),
    path('logout_user/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register_user'),
    
]