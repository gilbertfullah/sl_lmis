from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
    
    
class NewsAndEvents(models.Model):
    TAG = [
        ('', 'Select a Tag'),
        ('News', 'News'),
        ('Events', 'Events'),
    ]

    title = models.CharField(verbose_name="Title", max_length=250)
    author = models.CharField(verbose_name="Author", max_length=250)
    content = RichTextField()
    image1 = models.ImageField()
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    image5 = models.ImageField(blank=True)
    tag = models.CharField(verbose_name="Tag", max_length=200, choices=TAG)
    published_date = models.DateField(verbose_name="Published Date", default=timezone.now)
    created_at = models.DateField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
