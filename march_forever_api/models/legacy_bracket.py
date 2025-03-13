from django.db import models
from .league import League
from .team import Team
from .user import User

class LegacyBracket(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  league_id = models.ForeignKey(League, on_delete=models.CASCADE)
  champion_id = models.ForeignKey(Team, on_delete=models.CASCADE)
  points = models.IntegerField(default=0)
  key = models.BooleanField(default=False)
