from django.db import models
from core.models import RunTime, BusinessOwner



class Bot(models.Model):
    bot_username = models.CharField(max_length=33, unique=True)
    bot_id = models.BigIntegerField(unique=True)
    token = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(BusinessOwner, on_delete=models.CASCADE, to_field="telegram_id", related_name="bots")
    status = models.BooleanField(default=True)
    assignment = models.ForeignKey(RunTime, on_delete=models.SET_NULL, to_field="runtime_id", default=None, null=True, related_name="bots")

    def __str__(self):
        return self.bot_username