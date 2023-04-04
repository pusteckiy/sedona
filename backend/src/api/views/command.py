from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


from src.api.models import Command
from src.api.serializers.command import CommandSerializer, CreateCommandSerializer, AcceptCommandSerializer, CommandQuerySerializer


class CommandView(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    @staticmethod
    @swagger_auto_schema(
        tags=["Command"], 
        operation_summary="Получить список команд.", 
        query_serializer=CommandQuerySerializer, 
        responses={200: CommandSerializer(many=True)})
    def get(request):
        serializer = CommandQuerySerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        _all = serializer.data['all']
        if _all:
            commands = Command.objects.all()
        else:
            commands = Command.objects.filter(accepted=False)
            print(commands)
        print(_all)
        return Response(commands.values())

    @staticmethod
    @swagger_auto_schema(
        tags=["Command"], 
        operation_summary="Отправить команду на обработку.", 
        request_body=CreateCommandSerializer, 
        responses={201: CommandSerializer})
    def post(request):
        serializer = CreateCommandSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        command = serializer.save()
        return Response(CommandSerializer(command).data, status=status.HTTP_201_CREATED)


class CommandDetailView(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    @staticmethod
    @swagger_auto_schema(
        tags=["Command"],
        operation_summary="Получить информацию о команде",
        responses={200: CommandSerializer}
    )
    def get(_, command_id):
        command = get_object_or_404(Command, id=command_id)
        serializer = CommandSerializer(command)
        return Response(serializer.data)

    @staticmethod
    @swagger_auto_schema(
        tags=["Command"], 
        request_body=AcceptCommandSerializer, 
        responses={200: CommandSerializer})
    def put(request, command_id):
        serializer = AcceptCommandSerializer(data=request.data, context={"command_id": command_id})
        serializer.is_valid(raise_exception=True)
        command = serializer.save()
        return Response(CommandSerializer(command).data, status=status.HTTP_200_OK)
