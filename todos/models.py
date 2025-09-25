from django.db import models
from django.utils import timezone


# Create your models here.

class Events(models.Model):
    task = models.CharField(max_length=225)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)  
    due_date = models.DateField(null=True,blank=True)
    task_status = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.task}"