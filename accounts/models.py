from django.db import models

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
# Create your models here.
class UserDefaultAddress(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	shipping = models.ForeignKey("UserAdress", null=True, blank=True, on_delete=models.CASCADE)
	
	def __str__(self):
	 return str(self.user.username)


class UserAdress(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	address = models.CharField(max_length=120, null=True, blank=True)
	city = models.CharField(max_length=120, null=True, blank=True)
	state = models.CharField(max_length=120, null=True, blank=True)
	country = models.CharField(max_length=120)
	zip_code = models.CharField(max_length=25)
	phone = models.CharField(max_length=120)
	shipping = models.BooleanField(default=True)
	billing = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)


	def __str__(self):
		return str(self.user.username)
	def get_user_addresses(self):
		return "{},{},{},{},{}".format(self.address, self.city, self.state, self.country, self.zip_code)
	class Meta:
		ordering = ['-timestamp','-updated']

	
	


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
	activation_key = models.CharField(max_length=200, null = True, blank = True)
	confirmed = models.BooleanField(default=False)
	

	def __str__(self):
	 	return str(self.confirmed)
	def activate_user_email(self):
		activation_url = "{}{}".format(settings.SITE_URL, reverse('activation_view',args=[self.activation_key]))
		context = {
			"activation_key": self.activation_key,
			"activation_url":activation_url
		}
		message = render_to_string('accounts/activation_message.txt',context)
		subject = 'Confirm you email'
		print(message)
		self.email_the_user(subject,message, settings.DEFAULT_FROM_EMAIL)


	def email_the_user(self, subject, message, from_email=None, **kwargs):
		send_mail(subject,message,from_email,[self.user.email],kwargs)
	