from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from .models import Workouts ,  Exercise


# Create your views here.
class Home(TemplateView):
    template_name = "index.html"

class Dashboard(ListView):
    model = Workouts
    template_name = "dashboard.html"
    context_object_name ='workouts'

class About(TemplateView):
    template_name = "about.html"

class Register(TemplateView):
    template_name = "registration.html"

class Login(TemplateView):
    template_name = "login.html"

class ViewWorkout(ListView):
    model = Workouts
    template_name = "view.html"
    context_object_name ='detail_view'

class CreateWorkout(CreateView):
    model = Workouts
    fields = ['title', 'description', 'training_split']
    template_name = "create.html"
    success_url = '/dashboard/'

def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ErrorPage(TemplateView):
    template_name = "404.html" 


