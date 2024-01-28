from django.db import models
from django.utils import timezone

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created = models.DateTimeField(blank=True, auto_now_add=True)
    updated = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.username
