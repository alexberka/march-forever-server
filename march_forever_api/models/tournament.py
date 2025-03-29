from django.db import models

class Tournament(models.Model):
  name = models.CharField(max_length=255)
  submission_open = models.BooleanField(default=False)
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()
  key_type = models.CharField(max_length=100, default='T64R4')
  max_points = models.IntegerField(default=0)
