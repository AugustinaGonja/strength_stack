from django.shortcuts import render 
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Workouts , Exercise
from .forms import NewWorkoutForm

# Create your views here.
def Home(request):
    return render(request ,"index.html")

def Dashboard(request):
    workouts = Workouts.objects.all()
    return render(request, "dashboard.html", {"workouts": workouts})

def About(request):
    return render(request, "about.html")

def Register(request):
    return render(request, "registration.html")

def Login(request):
    return render(request, "login.html")

def ViewWorkout(request, view_id):
    workout = get_object_or_404(Workouts, id=view_id, user=request.user)
    return render(request, "view.html", {"workout": workout})

def CreateWorkout(request):
    if request.method == "POST":
        form = NewWorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('dashboard')
    else:
        form = NewWorkoutForm()
        return render(request, "create.html", {"form": form})

def DeleteWorkout(request, workout_id):
    if request.method == "POST":
        workout = get_object_or_404(Workouts, id=workout_id ,user=request.user)
        workout.delete()
    return redirect('dashboard')

#def UpdateWorkout(request):  
#def ErrorPage():
   #template_name = "404.html" 


