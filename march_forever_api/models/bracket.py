from django.db import models
from .box import Box
from .user import User

class Bracket(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  points = models.IntegerField(default=0)
  key = models.BooleanField(default=False)
