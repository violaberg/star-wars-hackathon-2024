from django.db import models
from cloudinary.models import CloudinaryField


class FAQ(models.Model):

    class Meta:
        """
        Customizes the display name of the category in the admin panel.
        """
        verbose_name_plural = 'Frequently Asked Questions'

    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Article(models.Model):
    """
    Model for knowledge sanctuary page
    """
    class Meta:
        verbose_name_plural = 'Articles'

    image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=200)
    body = models.TextField()
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title