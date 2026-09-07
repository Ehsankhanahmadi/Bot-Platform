from django.contrib import admin
from .models import RunTime, BusinessOwner, Bot

admin.site.register([RunTime,BusinessOwner,Bot])