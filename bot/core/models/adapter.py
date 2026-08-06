from django.db import models

class Adapter(models.Model):
    token = models.TextField(max_length=255, unique=True, default='')
    botid = models.TextField(max_length=100, unique=True, default='')

    def __str__(self):
        return self.botid