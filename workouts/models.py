from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Workouts 

class Workouts(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length= 200)
    description = models.SlugField(max_length= 200)
    created_on = models.DateTimeField(auto_now_add=True)

# Exercise

class Exercise(models.Model):
    workout = models.ForeignKey(Workouts, on_delete = models.CASCADE) 
    name = models.CharField(max_length= 100)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()