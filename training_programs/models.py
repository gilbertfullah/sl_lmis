from django.db import models
from django.utils import timezone

class Training(models.Model):
    TOPIC_CHOICES = [
        ('', 'Select a topic'),
        ('Computer Science, Data Modeling & Analytics', 'Computer Science, Data Modeling & Analytics'),
        ('Biotechnology & Pharmaceutical', 'Biotechnology & Pharmaceutical'),
        ('Design & Manufacturing', 'Design & Manufacturing'),
        ('Innovation', 'Innovation'),
        ('Real Estate', 'Real Estate'),
        ('Leadership & Communication', 'Leadership & Communication'),
        ('Crisis Management', 'Biotechnology & Pharmaceutical'),
        ('Energy & Sustainability', 'Energy & Sustainability'),
    ]
    
    LOCATION_CHOICES = (
        ('', 'Select a location'),
        ('Live Virtual', 'Live Virtual'),
        ('Hybrid', 'Hybrid'),
        ('On Campus', 'On Campus'),
    )
    
    STATUS_CHOICES = (
        ('', 'Select status'),
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    )
    
    course = models.CharField(max_length=200)
    course_description = models.TextField(null=True, blank=True)
    location = models.CharField(verbose_name="Location", max_length=200)
    status = models.CharField(verbose_name="Status", max_length=100, choices=STATUS_CHOICES)
    lead_instructor = models.CharField(max_length=200)
    fees = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField()
    topic = models.CharField(verbose_name="Topic", max_length=200, choices=TOPIC_CHOICES)
    learning_outcome = models.TextField(verbose_name="Learning Outcome", max_length=250, blank=True, null=True)
    curriculum = models.TextField(verbose_name="Curriculum", max_length=250, blank=True, null=True)
    updated = models.DateField(auto_now=True)
    created_at = models.DateField(default=timezone.now)
    
    class Meta:
        ordering = ['-updated', '-created_at']
    
    def __str__(self):
        return self.course




