from django.contrib import admin
from .models import Workouts, Exercise
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Workouts)

class WorkoutsAdmin(SummernoteModelAdmin):
    list_display = ('title', 'user', 'created_on')
    search_fields = ['title']
    list_filter = ('created_on',)
    #prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)

@admin.register(Exercise)

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'workout', 'sets' , 'reps')
    search_fields = ['name', 'workout__title']
    #list_filter = ('created_on',)
