from decouple import config

TOKEN = config('TOKEN')
API_TOKEN = config('API_TOKEN')

ADMIN_ID = config('ADMIN_ID', cast=int)
ADMIN_ROLE_ID = config('ADMIN_ROLE_ID', cast=int)
GUILD_ID = config('GUILD_ID', cast=int)
