from django.db import models
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    finish = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)