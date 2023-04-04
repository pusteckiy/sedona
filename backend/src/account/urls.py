from django.urls import path
from src.account import views

urlpatterns = [
    path('', views.account_main, name='main'),
    path('login', views.account_login, name='login'),
    path('redirect', views.account_login_redirect, name='redirect'),
    path('logout', views.account_logout, name='logout'),
    path('deposit', views.account_deposit, name='deposit'),
    path('connect', views.account_connect, name='connect'),
    path('connect/code', views.account_connect_code, name='connect-code'),
    path('clear-rakbot', views.account_clear_rakbot, name='account-clear-rakbot')
]
