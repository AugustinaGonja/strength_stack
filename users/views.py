from django.shortcuts import redirect, render, get_object_or_404
from .models import Profile
from .forms import ProfileForm

# Create your views here.


def UserProfile(request):
    user_info = Profile.objects.get(user=request.user)
    return render(request, "profile.html", {'user_info': user_info})


def UpdateProfile(request):
    user_info = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user_info)
        if form.is_valid():
            profile = form.save()
            profile.user = request.user
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_info)
    return render(request, "update_profile.html", {"form": form})

