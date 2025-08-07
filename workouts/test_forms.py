from django.test import TestCase
from .forms import NewWorkoutForm , UpdateWorkoutForm, ExerciseForm

# Create your tests here.

# Form Testing 
class TestNewWorkoutForm(TestCase):

    def test_form_is_valid(self):
        form = NewWorkoutForm(data={
            'title': 'Push Day',
            'description': 'Chest, Triceps & Shoulder Workout',
            'training_split': 'Push Day'
        })
        self.assertTrue(form.is_valid())

    def test_missing_title_field(self):
        form = NewWorkoutForm(data={
            'title': '',
            'description': 'Chest, Triceps & Shoulder Workout',
            'training_split': 'Push Day'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_missing_description_field(self):
        form = NewWorkoutForm(data={
            'title': 'Push Day',
            'description': '',
            'training_split': 'Push Day'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors)

class TestExerciseForm(TestCase):
    def test_form_is_valid(self):
        form = ExerciseForm(data={
            'name': 'Bicep Curls',
            'training_style': 'straightsets',
            'sets': 4,
            'reps': 12,
            'weight' : 10
        })
        self.assertTrue(form.is_valid())
    def test_integer_fields_empty(self):
        form = ExerciseForm(data={
            'name': 'Bicep Curls',
            'training_style': 'straightsets',
            'sets': '',
            'reps': '',
            'weight' : ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('sets', form.errors)
        self.assertIn('reps', form.errors)
        self.assertIn('weight', form.errors)