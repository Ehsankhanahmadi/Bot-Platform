from django.db import models



class RunTime(models.Model):
    runtime_id = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=False)
    bot_count = models.IntegerField(default=0)

    def __str__(self):
        return self.runtime_id