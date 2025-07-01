from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Workouts 

class Workouts(models.Model):
    title = models.CharField()
    content = models.TextField()
    created_on = models.DateTimeField()

# Exercise

class Exercise(models.Model):
    name = models.CharField()
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()