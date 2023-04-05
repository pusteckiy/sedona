import os
from pathlib import Path

import pytz
from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent.parent
SRC_DIR = os.path.join(BASE_DIR, 'src')


SECRET_KEY = config('DJANGO_SECRET_KEY')
GP_LOGIN = config('GP_LOGIN')
GP_PASSWORD = config('GP_PASSWORD')


ALLOWED_HOSTS = ['*']


AUTHENTICATION_BACKENDS = [
    'src.account.auth.DiscordAuthenticationBackend'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTIFICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication'
    ),

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),

    'EXCEPTION_HANDLER': 'src.api.exceptions.custom_exception_handler'
}

INSTALLED_APPS = [
    # Apps
    'src.api',
    'src.account',
    'src.shop',

    # Requirements
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'jazzmin',

    # Base
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

JAZZMIN_SETTINGS = {
    "site_title": "Sedona | Admins",
    "site_brand": "AdminPanel",
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SRC_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'SECURITY_REQUIREMENTS': [{
        'Token': []
    }]
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

AUTH_USER_MODEL = 'account.Profile'

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Kiev'
PYTZ_TIME_ZONE = pytz.timezone(TIME_ZONE)

USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
