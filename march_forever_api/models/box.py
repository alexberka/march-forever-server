from django.db import models
from .team import Team

class Box(models.Model):
  team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
  code = models.CharField(max_length=4)
