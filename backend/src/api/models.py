from django.db import models

# Create your models here.
class Command(models.Model):
    text = models.CharField(max_length=256)
    user = models.CharField(max_length=64)
    datetime = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
