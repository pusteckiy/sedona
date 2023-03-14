from django.urls import path
from src.account.views import *

urlpatterns = [
    path('', account_main, name='main'),
    path('login', account_login, name='login'),
    path('redirect', account_login_redirect, name='redirect'),
    path('logout', account_logout, name='logout'),
    path('deposit', account_deposit, name='deposit'),
    path('connect', account_connect, name='connect'),
    path('connect/code', account_connect_code, name='connect-code'),
]