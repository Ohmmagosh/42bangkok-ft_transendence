from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserStat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='stat')
    win = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str(self):
        return f'UserStat {self.user.username}'
    
    def update_win(self):
        self.win += 1
        pass
        
    def update_lose(self):
        self.lose += 1
        pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profile')
    nick_name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_images')
    friend_list = models.ManyToManyField(User)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['user']
    
    def __str__(self):
        return f'UserProfile: {self.id} {self.user.username}'
 