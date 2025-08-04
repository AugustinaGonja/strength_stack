from django import forms 
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['age', 'gender','current_weight','goal_weight','bio','profile_image',]
