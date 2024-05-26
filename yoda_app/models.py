from django.db import models
from cloudinary.models import CloudinaryField
from django_summernote.fields import SummernoteTextField
from django.utils.text import slugify


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
    body = SummernoteTextField()
    link = models.URLField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            # Ensure slug is unique
            unique_slug = self.slug
            num = 1
            while Article.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{self.slug}-{num}"
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)