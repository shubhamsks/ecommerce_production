from django.db import models

from django.conf import settings
# Create your models here.
class UserStripe(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	stripe_id = models.CharField(max_length = 120, null = True, blank = True)


	def __str__(self):
		return str(self.stripe_id)
# "cus_FlVH0dvFfHqn9m",
# cus_FlVWnhr4QXrfTl
# cus_FlVWnhr4QXrfTl

class EmailConfirmed(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	hashkey = models.CharField(max_length=200, null = True, blank = True)
	confirmed = models.BooleanField(default=False)
	

	def __str__(self):
	 return str(self.confirmed)