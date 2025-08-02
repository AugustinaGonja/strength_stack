from django.urls import path
from .import views

urlpatterns = [
    path('profile/', views.UserProfile, name='profile'),
    path('update_profile/', views.UpdateProfile , name='update_profile')
]