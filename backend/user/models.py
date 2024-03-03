from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserStat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    win = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str(self):
        return f'UserStat {self.user.first_name}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nick_name = models.CharField(max_length=255, null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'UserProfile: {self.id} {self.user.first_name} {self.user.last_name}'
 