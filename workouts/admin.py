from django.contrib import admin
from .models import Workouts, Exercise ,WorkoutDetails
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class ExerciseInline(admin.TabularInline):
    model = Exercise
    extra = 1

class WorkoutDetailsInline(admin.TabularInline):
    model = WorkoutDetails
    extra = 1

@admin.register(Workouts)

class WorkoutsAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created_on')
    search_fields = ['title']
    list_filter = ('created_on',)
    summernote_fields = ('description',)
    inlines = [ExerciseInline, WorkoutDetailsInline]

@admin.register(Exercise)

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'workout', 'sets' , 'reps',)
    search_fields = ['name', 'workout__title']
    list_filter = ('name',)

@admin.register(WorkoutDetails)
class WorkoutDetailsAdmin(admin.ModelAdmin):
    list_display = ('updated_on', 'created_on', 'workout_duration' , 'notes')