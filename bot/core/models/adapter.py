from django.db import models

class Adapter(models.Model):
    token = models.TextField(max_length=255, unique=True)
    botid = models.TextField(max_length=100, unique=True)

    def __str__(self):
        return self.botid