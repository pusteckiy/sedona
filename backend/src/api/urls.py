from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from src.api.views import RakBotCommand


shema_view = get_schema_view(
    openapi.Info(
        title='Sedona API',
        default_version='1.0.0'
    ),
    public=False
)

urlpatterns = [
    path('rak-bot/command', RakBotCommand.as_view()),
    path('docs/', shema_view.with_ui()),
]