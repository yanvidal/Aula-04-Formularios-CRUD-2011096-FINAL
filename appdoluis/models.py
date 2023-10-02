# https://docs.djangoproject.com/en/4.2/topics/db/models/

from django.db import models

class Movies(models.Model):
  title = models.CharField(max_length=50)
  director = models.CharField(max_length=70)
  genre = models.CharField(max_length=20)
  release_date = models.DateField()

class ThingsILike(models.Model):
  OPTIONS = [
    ("N", "Never"),
    ("S", "Sometimes"),
    ("A", "Always"),
  ]
  CATEGORY = [
    ("F", "Fun"),
    ("W", "Work"),
    ("H", "Health"),
  ]
  title = models.CharField(max_length=50)
  how_often = models.CharField(max_length=1, choices=OPTIONS)
  priority = models.IntegerField()
  category = models.CharField(max_length=1, choices=CATEGORY)