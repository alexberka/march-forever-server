from django.db import models

class Team(models.Model):
  school = models.CharField(max_length=255)
  nickname = models.CharField(max_length=255)
  abbreviation = models.CharField(max_length=5)
  logo_url = models.URLField()
  color_primary_hex = models.CharField(max_length=7)
  color_secondary_hex = models.CharField(max_length=7)
