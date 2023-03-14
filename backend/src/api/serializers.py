from rest_framework import serializers

from api.models import Command


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ('text', 'user', 'datetime', 'accepted')