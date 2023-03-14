from django.contrib import admin

from src.shop.models import Product, Category, PurchaseHistory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.name


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'category',)

    def __str__(self):
        return self.name


@admin.register(PurchaseHistory)
class PurchaseHistoryAdmin(admin.ModelAdmin):
    
    list_display = ('profile', 'product', 'delivered', 'time')
