from django.views.generic import ListView
from .models import Profile

# Create your views here.
class Profile(ListView):
    model = Profile
    template_name = "profile.html"

