# Generated by Django 4.2.23 on 2025-07-26 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='units',
            field=models.PositiveIntegerField(choices=[('kg', 'KILOGRAMS'), ('lbs', 'POUNDS')], default=55),
        ),
        migrations.AlterField(
            model_name='profile',
            name='current_weight',
            field=models.PositiveIntegerField(choices=[('kg', 'KILOGRAMS'), ('lbs', 'POUNDS')], default=64),
        ),
        migrations.AlterField(
            model_name='profile',
            name='goal_weight',
            field=models.PositiveIntegerField(default=55),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
