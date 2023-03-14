from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication

from src.api.models import Command


class RakBotCommand(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)


    def get(self, request):
        _all = request.data.get('all')
        if _all:
            commands = Command.objects.all().values()
        else: 
            commands = Command.objects.filter(accepted=False).values()
        return Response({'status': 'ok', 'commands': commands})
    

    def post(self, request):
        command_text = request.data.get('text')
        if command_text:
            Command.objects.create(
                text = command_text,
                user = request.user.id
            )
            return Response({'status': 'ok', 'message': 'Команда добавлена в БД.'})
        return Response({'status': 'error', 'message': 'Не передан аргумент `text`'})
    
    
    def patch(self, request):
        try:
            command = Command.objects.get(id=request.data['id'], accepted=False)
            command.accepted = True
            command.save()
            return Response({'status': 'ok', 'message': 'Форма принята.'})
        except:
            return Response({'status': 'error', 'message': 'Форма не найдена или уже принята.'})
