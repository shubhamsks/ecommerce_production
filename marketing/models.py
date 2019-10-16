from django.db import models

# Create your models here.
class MarketingMessage(models.Model):
    message = models.CharField(max_length=120)
    acitve = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auth_now_add = )