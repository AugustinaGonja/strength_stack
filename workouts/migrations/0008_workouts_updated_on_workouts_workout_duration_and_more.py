# Generated by Django 4.2.23 on 2025-07-26 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0007_workouts_user_alter_exercise_units_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workouts',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='workouts',
            name='workout_duration',
            field=models.PositiveIntegerField(blank=True, default=120, null=True),
        ),
        migrations.DeleteModel(
            name='WorkoutDetails',
        ),
    ]
