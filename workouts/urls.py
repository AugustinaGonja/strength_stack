from django.urls import include, path
from .import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('dashboard/', views.Dashboard, name='dash'),
    path('about/', views.About, name='about'),
    path('registration/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('view/', views.ViewWorkout, name='view'),
    path('create/', views.CreateWorkout, name='create'),
]

