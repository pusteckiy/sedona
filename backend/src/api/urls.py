from django.urls import path
from django.shortcuts import redirect

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from src.api.views import command, functions, account
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title='CyberSedona API',
        default_version='1.0.0',
    ),
    public=True,
    url=settings.APP_URL
)


urlpatterns = [
    path('rak-bot/status', command.StatusView.as_view(), name='status'),
    path('rak-bot/command', command.CommandView.as_view(), name='command'),
    path('rak-bot/command/<int:command_id>', command.CommandDetailView.as_view(), name='command-detail'),
    path('rak-bot/checkoff', functions.CheckoffView.as_view(), name='checkoff'),
    path('rak-bot/tranfer', functions.TransferMoneyView.as_view(), name='transfer'),
    path('rak-bot/clearbot', functions.ClearRakBotView.as_view(), name='clearbot'),
    path('account/<int:account_id>', account.AccountView.as_view(), name='account'),
    path('docs/', schema_view.with_ui(), name='docs'),
]
