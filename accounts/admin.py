from django.contrib import admin

# Register your models here.
from .models import UserStripe, UserAdress

admin.site.register(UserStripe)
admin.site.register(UserAdress)
