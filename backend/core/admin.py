from django.contrib import admin
from .models import User, Device, SensorReading, Action, Token

admin.site.register(User)
admin.site.register(Device)
admin.site.register(SensorReading)
admin.site.register(Action)
admin.site.register(Token)
