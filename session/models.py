from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Session(models.Model):
    CHARACTERS = [
        (0, 'Yoda1'),
        (1, 'Yoda2'),
        (3, 'Yoda3'),
        (4, 'Yoda4'),
        (5, 'Yoda5'),
    ]
    DIFFICULTY = [
        (0, 'Easy'),
        (1, 'Medium'),
        (3, 'Hard'),
    ]
    # session_name = models.CharField(max_length=200, unique=True)
    # slug = models.SlugField(max_length=200, unique=True)
    session_user = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="user_sessions")
    character = models.IntegerField(choices=CHARACTERS, default=0)
    level = models.IntegerField(choices=DIFFICULTY, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"Session user {self.session_user}"

class Character(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    image = CloudinaryField('image', default='placeholder')
    meditation_technique_one = models.TextField(blank=True)
    meditation_technique_two = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"Character name {self.name}"