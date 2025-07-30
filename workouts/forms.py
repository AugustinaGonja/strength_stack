from django import forms 
from .models import Workouts , Exercise

class NewWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workouts
        fields =['title', 'description', 'training_split']

class UpdateWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workouts
        fields =['title', 'description', 'training_split']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields =['name', 'training_style', 'sets', 'reps','weight','units']