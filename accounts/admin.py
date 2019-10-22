from django.contrib import admin

# Register your models here.
from .models import UserStripe, EmailConfirmed, UserAdress

admin.site.register(UserStripe)
admin.site.register(EmailConfirmed)
admin.site.register(UserAdress)
