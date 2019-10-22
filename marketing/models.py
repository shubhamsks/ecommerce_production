from django.db import models
from django.utils import timezone
class MarketingMessageQuerySet(models.query.QuerySet):

    def active(self):
        queryset = self.filter(active=True)
        return queryset
    def featured(self):
        queryset = self.filter(featured=True) \
            .filter(start_date__lte=timezone.now()) \
            .filter(end_date__gte=timezone.now())  
        return queryset
    
    

class MarketingMessageManager(models.Manager):
    def get_queryset(self):
        temp = MarketingMessageQuerySet(self.model, using=self._db)
        return temp
    def all(self):
        return self.get_queryset().active()
    def all_featured(self):
        return self.get_queryset().active().featured()
    def get_featured_item(self):
        message = self.get_queryset().active().featured()[0].message
        return message

class MarketingMessage(models.Model):
    message = models.CharField(max_length=120)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated  = models.DateTimeField(auto_now_add=False, auto_now=True)
    start_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    end_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    objects = MarketingMessageManager()
    messages = MarketingMessageManager()

    def __str__(self):
        return str(self.message[:10])
    class Meta:
        ordering = ['-start_date','-end_date']
    
def slider_upload(instance, filename):
    return "images/marketing/slider/%s"%(filename)

class Sliders(models.Model):
    image = models.ImageField(upload_to = slider_upload)
    order = models.IntegerField(default = 0)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    end_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    objects = MarketingMessageManager()

    def __str__(self):
        return str(self.image.name)
    class Meta:
        ordering = ['order']


    