from django.db import models

class User(models.Model):
  username = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  joined_on = models.DateTimeField(auto_now_add=True)
