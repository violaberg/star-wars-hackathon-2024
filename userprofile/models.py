from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    PADAWAN = 0
    JEDI_KNIGHT = 1
    JEDI_MASTER = 3
    DIFFICULTY_CHOICES = [
        (PADAWAN, 'Padawan'),
        (JEDI_KNIGHT, 'Jedi Knight'),
        (JEDI_MASTER, 'Jedi Master'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.IntegerField(choices=DIFFICULTY_CHOICES, default=PADAWAN)

    def __str__(self):
        return self.user.username

    def avatar_image(self):
        avatar_paths = {
            self.PADAWAN: 'images/avatars/padawan.png',
            self.JEDI_KNIGHT: 'images/jedi_knight.png',
            self.JEDI_MASTER: 'images/jedi_master.png',
        }
        return avatar_paths.get(self.avatar, 'images/placeholder.png')


class UserMeditationSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_name = models.CharField(max_length=200, unique=True)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-completed_at"]

    def __str__(self):
        return f"{self.user.username} - {self.session_name}"
