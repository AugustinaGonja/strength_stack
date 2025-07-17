from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Workouts 

TRAINING_STYLE = [
    ('straightsets', 'STRAIGHTSETS'),
    ('dropsets', 'DROPSETS'),
    ('clustersets', 'CLUSTERSETS'),
    ('pyramidsets', 'PYRAMIDsets'),
    ('timeundertension', 'TIMEUNDERTENSION'),
    ('other', 'OTHER'),
]

class Workouts(models.Model):
    title = models.CharField(max_length= 200)
    training_split = models.CharField(max_length= 200, default='Enter Split')
    description = models.CharField(max_length= 200, default='Enter Short Description')
    created_on = models.DateTimeField(auto_now_add=True)

# Exercise

class Exercise(models.Model):
    workout = models.ForeignKey(Workouts, on_delete = models.CASCADE) 
    name = models.CharField(max_length= 100)
    training_style = models.CharField(max_length= 50 , choices= TRAINING_STYLE , default = "split")
    sets = models.PositiveIntegerField(default=4)
    reps = models.PositiveIntegerField(default=12)
    weight = models.PositiveIntegerField(default=12)
    units = models.CharField(default= 'kg or lbs')