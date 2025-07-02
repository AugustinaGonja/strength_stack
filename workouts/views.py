from django.shortcuts import render
from django.views import generic
from .models import Workouts, Exercise

# Create your views here.
class Dashboard(generic.ListView):
    queryset = Workouts.objects.all()
    template_name = "workouts/dashboard.html"