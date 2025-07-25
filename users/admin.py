from django.contrib import admin

# Register your models here.
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)