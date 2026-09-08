from django.db import models
from core.models import RunTime, BusinessOwner



class Bot(models.Model):
    bot_username = models.CharField(max_length=32, unique=True)
    bot_id = models.BigIntegerField(unique=True)
    token = models.CharField(max_length=255)
    owner = models.ForeignKey(BusinessOwner, on_delete=models.CASCADE, related_name="bots")
    status = models.BooleanField(default=True)
    assignment = models.ForeignKey(RunTime, on_delete=models.SET_NULL, default=None, null=True, related_name="bots")

    def __str__(self):
        return self.bot_username