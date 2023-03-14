from django.contrib import admin
from rest_framework.authtoken.models import Token

from src.account.models import Profile, Deposit
from src.shop.models import PurchaseHistory


class DepositInline(admin.TabularInline):
    model = Deposit
    list_display = ()

class PurchaseHistoryInline(admin.TabularInline):
    model = PurchaseHistory
    list_display = ()

class TokenInline(admin.TabularInline):
    model = Token
    list_display = ()


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    fields = (('nickname', 'id'), ('money', 'coins'), ('verification_code', 'is_active'),)
    list_display = ('nickname', 'id',)

    inlines = [
        DepositInline,
        PurchaseHistoryInline,
        TokenInline,
    ]

    def __str__(self):
        return self.nickname
