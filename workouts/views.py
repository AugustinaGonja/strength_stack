from django.views.generic import ListView, TemplateView
from .models import Workouts, Exercise

# Create your views here.
class Dashboard(ListView):
    model = Workouts
    template_name = "dashboard.html"

class Home(TemplateView):
    template_name = "index.html"