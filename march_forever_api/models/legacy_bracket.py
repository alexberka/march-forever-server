from django.db import models
from .league_tournament import LeagueTournament
from .team import Team
from .user import User

class LegacyBracket(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='legacy_brackets')
  league_tournament_id = models.ForeignKey(LeagueTournament, on_delete=models.CASCADE, related_name='legacy_brackets')
  champion_id = models.ForeignKey(Team, on_delete=models.CASCADE)
  points = models.IntegerField(default=0)
