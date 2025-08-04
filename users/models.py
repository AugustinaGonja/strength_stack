from django.db import models
from django.contrib.auth.models import User
# Create your models here.
GENDER = [
    ('Male', 'MALE'),
    ('Female', 'FEMALE'),
    ('Other', 'OTHER'),
]

UNITS = [
    (1, 'kg'),
    (2, 'lbs'),
]
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) 
    age = models.PositiveIntegerField(default= 24)
    gender = models.CharField(max_length= 50 , choices= GENDER ,  default = "male")
    current_weight = models.PositiveIntegerField(default=64)
    goal_weight = models.PositiveIntegerField(default=55)
    units = models.PositiveIntegerField(default=1, choices = UNITS,)
    bio = models.TextField(default= 'Provide description about yourself and your fitness goals.')
    profile_image = models.ImageField(null=True , blank =True, upload_to ="images/")

    def __str__(self):
        return f"{self.user}'s Profile"
    