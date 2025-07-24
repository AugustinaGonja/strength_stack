from django.views.generic import ListView, TemplateView
from .models import Workouts, Exercise

# Create your views here.
class Home(TemplateView):
    template_name = "index.html"

class Dashboard(ListView):
    model = Workouts
    template_name = "dashboard.html"

class About(TemplateView):
    template_name = "about.html"

class Register(TemplateView):
    template_name = "registartion.html"