from django.db import models
from .user import User
from .tournament import Tournament

class League(models.Model):
  name = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  admin_id = models.ForeignKey(User, on_delete=models.CASCADE)
  users = models.ManyToManyField(User, through="UserLeague", related_name="leagues")
  tournaments = models.ManyToManyField(Tournament, through="LeagueTournament", related_name="leagues")
