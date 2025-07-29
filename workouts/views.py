from django.shortcuts import render 
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Workouts 

# Create your views here.
def Home(request):
    return render(request ,"index.html")

def Dashboard(request):
    workouts = Workouts.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"workouts: workouts"})

def About(request):
    return render(request, "about.html")

def Register(request):
    return render(request, "registration.html")

def Login(request):
    return render(request, "login.html")

def ViewWorkout(request, pk):
    workout = get_object_or_404(Workouts, pk=pk, user=request.user)
    return render(request, "view.html", {"workout": workout})

#def CreateView(request):

def ErrorPage():
    template_name = "404.html" 


