import os
from pathlib import Path

import pytz
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = os.path.join(BASE_DIR, 'src')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
GP_LOGIN = config('GP_LOGIN')
GP_PASSWORD = config('GP_PASSWORD')

DOMAIN_IP = '127.0.0.1:8000' if DEBUG else 'cyber-sedona.fun'
DISCORD_REDIRECT_URL = f"https://discord.com/api/oauth2/authorize?client_id=821736713231007765&redirect_uri=https%3A%2F%2F{DOMAIN_IP}%2Faccount%2Fredirect&response_type=code&scope=identify"


ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [f'https://{DOMAIN_IP}', f'http://{DOMAIN_IP}']


AUTHENTICATION_BACKENDS = [
    'src.account.auth.DiscordAuthenticationBackend'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTIFICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication'
    ),

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'src.api',
    'src.account',
    'src.shop',
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

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sedona',
        'USER': 'postgres',
        'PASSWORD': 'meloncikyt753',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'account.Profile'

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'
PYTZ_TIME_ZONE = pytz.timezone(TIME_ZONE)

USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
