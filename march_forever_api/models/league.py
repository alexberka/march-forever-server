from django.db import models
from .user import User

class League(models.Model):
  name = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  admin_id = models.ForeignKey(User, on_delete=models.CASCADE)
