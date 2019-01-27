from django.contrib import admin
from .models import Service, Device, RawData, Rate, GoalRate

# Register your models here.

admin.site.register(Service)
admin.site.register(Device)
admin.site.register(RawData)
admin.site.register(Rate)
admin.site.register(GoalRate)
