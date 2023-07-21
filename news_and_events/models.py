from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

class Image(models.Model):
    images = ArrayField(models.ImageField(upload_to='news/', blank=True, null=True))
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f'Image Gallery {self.pk}'


class NewsAndEvents(models.Model):
    TAG = [
        ('', 'Select a Tag'),
        ('News', 'News'),
        ('Events', 'Events'),
    ]
    images = models.ForeignKey(Image, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title", max_length=250)
    author = models.CharField(verbose_name="Author", max_length=250)
    content = models.TextField(verbose_name="Content")
    tag = models.CharField(verbose_name="Tag", max_length=200, choices=TAG)
    published_date = models.DateField(verbose_name="Published Date", default=timezone.now)
    created_at = models.DateField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

