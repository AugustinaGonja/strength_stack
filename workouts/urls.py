from django.urls import include, path
from .import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('about/', views.About, name='about'),
    path('registration/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('view/<int:view_id>/', views.ViewWorkout, name='view'),
    path('create/', views.CreateWorkout, name='create'),
    path('delete/<int:workout_id>/', views.DeleteWorkout , name='delete'),
    path('update_workout/<int:workout_id>/', views.UpdateWorkout , name='update_workout'),
    path('update_exercise/<int:exercise_id>/', views.UpdateExercise , name='update_ex'),
    path('add_exercise/<int:workout_id>/', views.AddExercise , name='add_ex'),
    path('delete_exercise/<int:exercise_id>/', views.DeleteExercise , name='delete_ex'),
]

