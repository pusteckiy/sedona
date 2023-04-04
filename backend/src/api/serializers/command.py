from rest_framework import serializers
from django.shortcuts import get_object_or_404

from src.api.models import Command


class CommandQuerySerializer(serializers.Serializer):
    all = serializers.BooleanField(default=False)


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ('__all__')


class CreateCommandSerializer(serializers.Serializer):
    text = serializers.CharField()

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        return Command.objects.create(text=validated_data["text"], user=user_id)


class AcceptCommandSerializer(serializers.Serializer):
    json = serializers.JSONField()

    def create(self, validated_data):
        command = get_object_or_404(Command, id=self.context["command_id"])
        command.response = validated_data["json"]
        command.accepted = True
        command.save()
        return command
