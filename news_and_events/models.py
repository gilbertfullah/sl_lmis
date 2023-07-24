from django.db import models
from django.utils import timezone
    
    
class NewsAndEvents(models.Model):
    TAG = [
        ('', 'Select a Tag'),
        ('News', 'News'),
        ('Events', 'Events'),
    ]

    title = models.CharField(verbose_name="Title", max_length=250)
    author = models.CharField(verbose_name="Author", max_length=250)
    content = models.TextField(verbose_name="Content")
    image1 = models.FileField()
    image2 = models.FileField(blank=True)
    image3 = models.FileField(blank=True)
    image4 = models.FileField(blank=True)
    image5 = models.FileField(blank=True)
    tag = models.CharField(verbose_name="Tag", max_length=200, choices=TAG)
    published_date = models.DateField(verbose_name="Published Date", default=timezone.now)
    created_at = models.DateField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
