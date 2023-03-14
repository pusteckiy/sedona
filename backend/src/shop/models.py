from django.db import models
from src.account.models import Profile


CURRENCY_CHOICES = (
    ("SA$", "SA$"),
    ("SC", "SC"),
)

class Category(models.Model):
    name = models.CharField(max_length=64)
    photo = models.ImageField(upload_to='shop/category')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=256, blank=True, default='')
    photo = models.ImageField(upload_to='shop/product')
    price = models.IntegerField()
    currency = models.CharField(max_length=9, choices=CURRENCY_CHOICES, default="SC")
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class PurchaseHistory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    delivered = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    currency = models.CharField(max_length=9, choices=CURRENCY_CHOICES, default="SC")
