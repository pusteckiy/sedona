from decouple import config

TOKEN = config('TOKEN')
API_TOKEN = config('API_TOKEN')

ADMIN_ID = config('ADMIN_ID', cast=int)
MANAGEMENT_ADMIN_ROLE_ID = config('MANAGEMENT_ADMIN_ROLE_ID', cast=int)
LVL_4_ADMIN_ROLE_ID = config('LVL_4_ADMIN_ROLE_ID', cast=int)
LVL_3_ADMIN_ROLE_ID = config('LVL_3_ADMIN_ROLE_ID', cast=int)
GUILD_ID = config('GUILD_ID', cast=int)
