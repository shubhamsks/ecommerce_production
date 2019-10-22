from django.contrib import admin

# Register your models here.
from .models import MarketingMessage, Sliders

class MarketingMessageAdmin(admin.ModelAdmin):
    list_display = ['__str__','start_date','end_date','featured','active']
    class Meta:
        model = MarketingMessage

admin.site.register(MarketingMessage, MarketingMessageAdmin)



class SlidersAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'order', 'featured', 'active', 'start_date', 'end_date']
    list_editable = ['order','featured','active','start_date','end_date']
    class Meta:
        model = Sliders
admin.site.register(Sliders, SlidersAdmin)