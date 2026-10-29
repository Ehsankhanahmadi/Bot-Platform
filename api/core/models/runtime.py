import uuid
from django.db import models



class RunTime(models.Model):
    class RuntimeType(models.TextChoices):
        CHILD = "child", "Child Runtime"
        MOTHER = "mother", "Mother Runtime"
    runtime_type = models.CharField(default=RuntimeType.CHILD,max_length=10,choices=RuntimeType.choices)
    runtime_id = models.CharField(max_length=50,unique=True)
    password = models.UUIDField(default=uuid.uuid4,unique=True,null=True,blank=True)
    token = models.CharField(max_length=255,unique=True,null=True,blank=True)
    url = models.URLField(unique=True,null=True,blank=True)
    status = models.BooleanField(default=False)
    bot_count = models.IntegerField(default=0)

    def __str__(self):
        return self.runtime_id