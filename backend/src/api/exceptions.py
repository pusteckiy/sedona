from django.http import Http404
from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    if isinstance(exc, NotAuthenticated):
        return Response({'status': 'error', 'message': 'Отсутсвует авторизация.'}, status=status.HTTP_401_UNAUTHORIZED)

    if isinstance(exc, AuthenticationFailed):
        return Response({'status': 'error', 'message': 'Ошибка авторизации.'}, status=status.HTTP_401_UNAUTHORIZED)
    
    if isinstance(exc, Http404):
        return Response({'status': 'error', 'message': 'Запись не найдена.'}, status=status.HTTP_404_NOT_FOUND)
    
    return exception_handler(exc, context)
