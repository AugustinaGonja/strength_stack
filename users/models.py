from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name= 'user', on_delete = models.CASCADE) 
    age = models.PositiveIntegerField(default= 24)
    gender = models.CharField(max_length= 50 , default = "m/f")
    current_weight = models.PositiveIntegerField(default=4)
    goal_weight = models.PositiveIntegerField(default=12)

    