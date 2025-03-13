from django.db import models
from .user import User
from .league import League

class UserLeague(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  league_id = models.ForeignKey(League, on_delete=models.CASCADE)
  joined_on = models.DateTimeField(auto_now_add=True)
  retired = models.BooleanField(default=False)
