from django.db import models
from django.utils import timezone
#from django.contrib.postgres.fields import ArrayField


class NewsAndEvents(models.Model):
    TAG = [
        ('', 'Select a Tag'),
        ('News', 'News'),
        ('Events', 'Events'),
    ]
    #images = models.ForeignKey(Image, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title", max_length=250)
    author = models.CharField(verbose_name="Author", max_length=250)
    content = models.TextField(verbose_name="Content")
    tag = models.CharField(verbose_name="Tag", max_length=200, choices=TAG)
    published_date = models.DateField(auto_now_add=True)
    #created_at = models.DateField(default=timezone.now)
    
    class Meta:
        ordering = ['-published_date']
    
    def __str__(self):
        return self.title

