from django.db import models
from django.contrib.auth.models import User
# Create your models here.
GENDER = [
    ('male', 'MALE'),
    ('female', 'FEMALE'),
    ('other', 'OTHER'),
]

UNITS = [
    ('kg', 'KILOGRAMS'),
    ('lbs', 'POUNDS'),
]
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) 
    age = models.PositiveIntegerField(default= 24)
    gender = models.CharField(max_length= 50 , choices= GENDER ,  default = "m/f")
    current_weight = models.PositiveIntegerField(default=64, choices = UNITS,)
    goal_weight = models.PositiveIntegerField(default=55)
    units = models.PositiveIntegerField(default=55, choices = UNITS,)
    bio = models.TextField(default= 'Provide description about yourself and fitness goals.')

    def __str__(self):
        return f"{self.user}'s Profile"
    