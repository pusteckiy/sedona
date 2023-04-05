from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from src.api.serializers.account import AccountSerializer
from src.account.models import Profile


class AccountView(APIView):
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    @staticmethod
    @swagger_auto_schema(
        tags=["Account"], 
        operation_summary="Получить список команд.",
        responses={200: AccountSerializer})
    def get(request, account_id):
        profile = get_object_or_404(Profile, id=account_id)
        return Response(AccountSerializer(profile).data)