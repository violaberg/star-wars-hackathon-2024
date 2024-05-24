from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
    CHARACTERS = [
        (0, 'Yoda1'),
        (1, 'Yoda2'),
        (3, 'Yoda3'),
        (4, 'Yoda4'),
        (5, 'Yoda5'),
    ]
    session_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    session_user = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="user_sessions")
    character = models.IntegerField(choices=CHARACTERS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_on", "session_user"]
    
    def __str__(self):
        return f"{self.session_name} | Session user {self.session_user}"
