from django.urls import path

from src.shop.views import *


urlpatterns = [
    path('', shop_main, name='main'),
    path('buy/<int:product_id>', shop_buy_product, name='buy')
]