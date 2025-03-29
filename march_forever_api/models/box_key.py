from django.db import models
from .tournament import Tournament
from .team import Team

class BoxKey(models.Model):
  tournament_id = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='key')
  code = models.CharField(max_length=4)
  team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
