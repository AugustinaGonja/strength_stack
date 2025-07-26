from django.views.generic import ListView, TemplateView
from .models import Workouts ,  Exercise, WorkoutDetails

# Create your views here.
class Home(TemplateView):
    template_name = "index.html"

class Dashboard(ListView):
    model = Workouts
    template_name = "dashboard.html"

class About(TemplateView):
    template_name = "about.html"

class Register(TemplateView):
    template_name = "registration.html"

class ViewWorkout(ListView):
    model = Workouts ,Exercise, WorkoutDetails
    template_name = "view.html"

class ErrorPage(TemplateView):
    template_name = "404.html" 