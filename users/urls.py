from django.urls import include, path
from .import views

urlpatterns = [
    path('profile/', views.Profile, name='user_profile'),
]