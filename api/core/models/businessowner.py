from django.db import models



class BusinessOwner(models.Model):
    user_name = models.CharField(max_length=33, unique=True)
    telegram_id = models.BigIntegerField(unique=True)
    adapter_name = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.user_name