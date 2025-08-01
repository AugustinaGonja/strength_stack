from django.shortcuts import render, get_object_or_404
from .models import Profile

# Create your views here.
def UserProfile(request):
    user_info = Profile.objects.get(user=request.user)
    return render(request, "profile.html", {'user_info': user_info})

