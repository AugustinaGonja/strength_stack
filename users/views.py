from django.shortcuts import render, get_object_or_404
from .models import Profile

# Create your views here.
def Profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, "profile.html", {"profile": profile})

