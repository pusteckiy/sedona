from rest_framework import serializers

from src.account.models import Profile


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'nickname', 'money', 'coins', 'is_staff', 'is_active')
