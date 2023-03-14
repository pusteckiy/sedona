from django.db import models

from src.account.managers import DiscordUserOAuth2Manager


class Profile(models.Model):
	objects = DiscordUserOAuth2Manager()

	id = models.BigIntegerField(primary_key=True)
	avatar = models.CharField(max_length=100, null=True)
	nickname = models.CharField(max_length=64, null=True, blank=True)
	money = models.IntegerField(default=0)
	coins = models.IntegerField(default=0)
	last_login = models.DateTimeField(null=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)
	verification_code = models.IntegerField(default=0)

	REQUIRED_FIELDS = ['nickname']
	USERNAME_FIELD = 'id'


	def get_username(self):
		if self.is_active:
			return self.nickname
		return str(self.id)
	
	def __str__(self):
		return self.get_username()

	def has_permission(self):
		return self.is_staff
	
	def has_module_perms(self, app):
		return self.is_staff
	
	def has_perm(self, app):
		return self.is_staff
	
	def get_all_permissions(self):
		return []
	
	@property
	def is_authenticated(self):
		return True
	
	@property
	def is_anonymous(self):
		return False


class Deposit(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	string = models.CharField(max_length=256)
	time = models.DateTimeField(auto_now_add=True)
