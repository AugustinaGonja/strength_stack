from django import forms 
from .models import Workouts

class NewWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workouts
        fields =['title', 'description', 'training_split']