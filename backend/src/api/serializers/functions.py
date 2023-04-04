from rest_framework import serializers

from src.api.models import Command


class CheckoffSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)

    def create(self, validated_data):
        command_text = f">> checkoff {validated_data['username']}"
        user_id = self.context['request'].user.id
        return Command.objects.create(text=command_text, user=user_id)


class TransferMoneySerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    amount = serializers.IntegerField()

    def create(self, validated_data):
        return Command.objects.create(
            text=f">> sendmoney {validated_data['username']} {validated_data['amount']}",
            user=self.context['request'].user.id
        )


class ClearRakBotSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    ip = serializers.IPAddressField(protocol='IPv4')

    def create(self, validated_data):
        return Command.objects.create(
            text=f">> clearrakbot {validated_data['username']} {validated_data['ip']}",
            user=self.context['request'].user.id
        )


class ResponseSerializer(serializers.Serializer):
    status = serializers.CharField(default='ok')
    id = serializers.IntegerField()
