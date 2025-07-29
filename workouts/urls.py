from django.urls import include, path
from .import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('about/', views.About, name='about'),
    path('registration/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('view/<int:pk>/', views.ViewWorkout, name='view'),
    path('create/', views.CreateWorkout, name='create'),
    path('delete/<int:workout_id>/', views.DeleteWorkout , name='delete'),
]

