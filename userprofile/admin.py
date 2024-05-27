from django.contrib import admin
from .models import UserProfile, UserMeditationSession


admin.site.register(UserProfile)
admin.site.register(UserMeditationSession)
