from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Workouts 

TRAINING_STYLE = [
    ('straightsets', 'STRAIGHTSETS'),
    ('dropsets', 'DROPSETS'),
    ('clustersets', 'CLUSTERSETS'),
    ('pyramidsets', 'PYRAMIDSETS'),
    ('timeundertension', 'TIMEUNDERTENSION'),
    ('other', 'OTHER'),
]

UNITS = [
    ('kg', 'KILOGRAMS'),
    ('lbs', 'POUNDS'),
]

class Workouts(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE) 
    title = models.CharField(max_length= 200)
    workout_duration = models.PositiveIntegerField(default= 120 ,null=True , blank=True)
    training_split = models.CharField(max_length= 200, default='e.g Upper Body, Lower Body , PPL')
    description = models.TextField(default='Enter Short Description', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Exercise

class Exercise(models.Model):
    workout = models.ForeignKey(Workouts, on_delete = models.CASCADE, related_name= 'exercises') 
    name = models.CharField(max_length= 100)
    training_style = models.CharField(max_length= 50 , choices= TRAINING_STYLE , default = "split")
    sets = models.PositiveIntegerField(default=4)
    reps = models.PositiveIntegerField(default=12)
    weight = models.PositiveIntegerField(default=12)
    units = models.CharField(max_length=20, choices= UNITS ,default= 'kg or lbs')
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f" {self.name} - {self.sets} x {self.reps}"

