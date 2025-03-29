from django.db import models
from .box import Box
from .league_tournament import LeagueTournament
from .user import User

class Bracket(models.Model):
  name = models.CharField(max_length=100)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='brackets')
  league_tournament_id = models.ForeignKey(LeagueTournament, on_delete=models.CASCADE, related_name='brackets')
  points = models.IntegerField(default=0)
