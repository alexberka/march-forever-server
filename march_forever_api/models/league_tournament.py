from django.db import models
from .league import League
from .tournament import Tournament

class LeagueTournament(models.Model):
  league_id = models.ForeignKey(League, on_delete=models.CASCADE)
  tournament_id = models.ForeignKey(Tournament, on_delete=models.CASCADE)
  brackets_per_user = models.IntegerField(default=1)
