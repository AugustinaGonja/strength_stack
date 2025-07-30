from django.urls import include, path
from .import views

urlpatterns = [
    path('profile/', views.UserProfile, name='profile'),
]