from django.contrib.auth.backends import BaseBackend

from src.account.models import Profile


class DiscordAuthenticationBackend(BaseBackend):
    def authenticate(self, _, discord_user) -> Profile:
        print(discord_user)
        try:
            user = Profile.objects.get(id=discord_user['id'])
            if user.avatar != discord_user['avatar']:
                user.avatar = discord_user['avatar']
                user.save()
        except:
            user = Profile.objects.create_new_discord_user(discord_user)
        return user

    def get_user(self, user_id):
        try:
            return Profile.objects.get(pk=user_id)
        except Profile.DoesNotExist:
            return None
