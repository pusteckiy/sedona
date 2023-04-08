from .base import *

DEBUG = False


DOMAIN = 'cyber-sedona.fun'
DISCORD_REDIRECT_URL = f"https://discord.com/api/oauth2/authorize?client_id=821736713231007765&redirect_uri=https%3A%2F%2F{DOMAIN}%2Fredirect&response_type=code&scope=identify"
CSRF_TRUSTED_ORIGINS = [f'https://{DOMAIN}', f'http://{DOMAIN}']
APP_URL = f'https://{DOMAIN}'

DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = "5432"
DATABASE_PASSWORD = config('DATABASE_PASSWORD')
DATABASE_NAME = config('DATABASE_NAME')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sedona',
        'USER': 'postgres',
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': '5432',
    }
}


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
