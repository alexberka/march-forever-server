from django.db import models
from .team import Team
from .bracket import Bracket

class Box(models.Model):
  bracket_id = models.ForeignKey(Bracket, on_delete=models.CASCADE)
  team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
  code = models.CharField(max_length=4)
