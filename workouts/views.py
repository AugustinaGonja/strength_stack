from django.shortcuts import render, get_object_or_404, redirect
from .models import Workouts, Exercise
from .forms import NewWorkoutForm, UpdateWorkoutForm, ExerciseForm


# Create your views here.
def Home(request):
    return render(request, "index.html")


def Dashboard(request):
    workouts = (
        Workouts.objects.filter(user=request.user)
        .all()
        .order_by('-updated_on')
    )
    return render(request, "dashboard.html", {"workouts": workouts})


def About(request):
    return render(request, "about.html")


def Register(request):
    return render(request, "registration.html")


def Login(request):
    return render(request, "login.html")


def ViewWorkout(request, view_id):
    workout = get_object_or_404(Workouts, id=view_id)
    exercises = workout.exercises.all().order_by('updated_on')
    return render(
        request,
        "view.html",
        {"workout": workout, 'exercises': exercises}
    )


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
        workout = get_object_or_404(Workouts, id=workout_id)
        workout.delete()
    return redirect('dashboard')


def DeleteExercise(request, exercise_id):
    if request.method == "POST":
        exercise = get_object_or_404(Exercise, id=exercise_id)
        exercise.delete()
    return redirect('view', view_id=exercise.workout.id)


def UpdateWorkout(request, workout_id):
    workout = get_object_or_404(Workouts, id=workout_id)
    if request.method == "POST":
        form = UpdateWorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UpdateWorkoutForm(instance=workout)
    return render(request, "update_workout.html", {"form": form})


def AddExercise(request, workout_id):
    workout = get_object_or_404(Workouts, id=workout_id)
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.workout = workout
            exercise.save()
            return redirect('view', view_id=workout.id)
    else:
        form = ExerciseForm()
    return render(
        request,
        "add_exercise.html",
        {"form": form, "workout": workout}
    )


def UpdateExercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    if request.method == "POST":
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('view', view_id=exercise.workout.id)
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, "update_exercise.html", {"form": form})


def ErrorPage(request):
    return render(request, "404.html")

def ErrorPage500(request):
    return render(request, "500.html")