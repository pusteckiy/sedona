from django.contrib.auth import models
from rest_framework.authtoken.models import Token

class DiscordUserOAuth2Manager(models.UserManager):

	def create_new_discord_user(self, user):
		new_user = self.create(
			id=user['id'],
			avatar=user['avatar'],
		)
		Token.objects.create(user=new_user)
		return new_user
