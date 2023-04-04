from django.urls import path
from django.shortcuts import redirect

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from src.api.views import command, functions
from config.settings import DOMAIN

schema_view = get_schema_view(
    openapi.Info(
        title='CyberSedona API',
        default_version='1.0.0',
    ),
    public=True,
    url=f'https://{DOMAIN}'
)


urlpatterns = [
    path('rak-bot/command', command.CommandView.as_view(), name='command'),
    path('rak-bot/command/<int:command_id>',
         command.CommandDetailView.as_view(), name='command-detail'),
    path('rak-bot/checkoff', functions.CheckoffView.as_view(), name='checkoff'),
    path('rak-bot/tranfer', functions.TransferMoneyView.as_view(), name='transfer'),
    path('rak-bot/clearbot', functions.ClearRakBotView.as_view(), name='clearbot'),
    path('docs/', schema_view.with_ui(), name='docs'),
]
