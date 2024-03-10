from django.db import models
from django.contrib.auth.models import User
from user.models import UserStat
from django.shortcuts import get_object_or_404

# Create your models here.
class MatchInfo(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user2')
    isUser1Win = models.BooleanField(default=0)
    isUser2Win = models.BooleanField(default=0)
    score_user1 = models.IntegerField(default=0)
    score_user2 = models.IntegerField(default=0)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Match: [{self.user1.username}] vs [{self.user2.username}]'
    
    def update_match(self, wid, score1, score2):
        winner = get_object_or_404(User, pk=wid)
        self.score_user1 = score1
        self.score_user2 = score2
        if winner is self.user1:
            self.isUser1Win = True
            self.isUser2Win = False
        else:
            self.isUser1Win = False
            self.isUser2Win = True
        print(winner.stat.win)
        winner.stat.update_win()
        print(winner.stat.win)
        winner.stat.save()
        return f'{self.user1.username} [{self.score_user1}] vs [{self.score_user2}] {self.user2.username}'