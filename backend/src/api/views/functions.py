from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from drf_yasg.utils import swagger_auto_schema

from src.api.serializers.functions import CheckoffSerializer, TransferMoneySerializer, ClearRakBotSerializer, ResponseSerializer


class CheckoffView(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    @staticmethod
    @swagger_auto_schema(
        tags=["Functions"],
        operation_summary="Проверяет статистику игрока с помощью /checkoff",
        query_serializer=CheckoffSerializer,
        responses={201: ResponseSerializer}
    )
    def post(request):
        serializer = CheckoffSerializer(
            data=request.GET, context={'request': request})
        serializer.is_valid(raise_exception=True)
        command = serializer.save()
        return Response({'status': 'ok', 'id': command.id})


class TransferMoneyView(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    @staticmethod
    @swagger_auto_schema(
        tags=["Functions"],
        operation_summary="Переводит деньги с аккаунта игроку по нику",
        query_serializer=TransferMoneySerializer,
        responses={201: ResponseSerializer}
    )
    def post(request):
        serializer = TransferMoneySerializer(
            data=request.GET, context={'request': request})
        serializer.is_valid(raise_exception=True)
        command = serializer.save()
        return Response(ResponseSerializer(command).data)


class ClearRakBotView(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser)

    @staticmethod
    @swagger_auto_schema(
        tags=["Functions"],
        operation_summary="Снимает ракбота с игрока",
        query_serializer=ClearRakBotSerializer,
        responses={201: ResponseSerializer}
    )
    def post(request):
        serializer = TransferMoneySerializer(
            data=request.GET, context={'request': request})
        serializer.is_valid(raise_exception=True)
        command = serializer.save()
        return Response(ResponseSerializer(command).data)