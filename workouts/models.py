from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Workouts 

class Workouts(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    title = models.CharField(max_length= 200)
    description = models.CharField(max_length= 200, default='Enter Short Description')
    created_on = models.DateTimeField(auto_now_add=True)

# Exercise

class Exercise(models.Model):
    workout = models.ForeignKey(Workouts, on_delete = models.CASCADE) 
    name = models.CharField(max_length= 100)
    sets = models.PositiveIntegerField(default=4)
    reps = models.PositiveIntegerField(default=12)
    