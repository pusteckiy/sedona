from django.db import models


class Command(models.Model):
    text = models.CharField(max_length=255)
    response = models.JSONField(default=dict, blank=True)
    user = models.CharField(max_length=64, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)


class Status(models.Model):
    value = models.BooleanField()
    last_update = models.DateTimeField(auto_now=True)
