from .base import *

DEBUG = True

DOMAIN = '127.0.0.1:8000'
DATABASE_HOST = '127.0.0.1'
DISCORD_REDIRECT_URL = f"https://discord.com/api/oauth2/authorize?client_id=821736713231007765&redirect_uri=https%3A%2F%2F{DOMAIN}%2Fredirect&response_type=code&scope=identify"
CSRF_TRUSTED_ORIGINS = [f'https://{DOMAIN}', f'http://{DOMAIN}']
APP_URL = f'http://{DOMAIN}'

DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = "5432"
DATABASE_PASSWORD = config('DATABASE_PASSWORD')
DATABASE_NAME = config('DATABASE_NAME')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sedona',
        'USER': 'postgres',
        'PASSWORD': 'meloncikyt753',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static", 'static']
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = "/media/"
MEDIAFILES_DIRS = [BASE_DIR / "media", 'media']
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
