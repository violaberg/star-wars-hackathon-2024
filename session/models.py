from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Session(models.Model):
    """
    User sessions model
    """
    DIFFICULTY = [
        (0, 'Padawan'),
        (1, 'Jedi Knight'),
        (3, 'Jedi Master'),
    ]
    session_user = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="user_sessions")
    character = models.CharField(max_length=200, blank=False)
    level = models.IntegerField(choices=DIFFICULTY, default=0)
    medition_selected = models.CharField(max_length=200, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"Session user {self.session_user}"


class Character(models.Model):
    """
    Star wars Characters model
    """
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    image = CloudinaryField('image', default='placeholder')
    med_one = CloudinaryField('med_1', default='placeholder')
    med_two = CloudinaryField('med_2', default='placeholder')
    meditation_one_name =  models.CharField(max_length=200)
    meditation_two_name =  models.CharField(max_length=200)
    meditation_technique_one = models.TextField(blank=True)
    meditation_technique_two = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return self.name
