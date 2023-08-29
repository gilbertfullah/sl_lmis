from django.db import models
from ckeditor.fields import RichTextField

class LFP(models.Model):
    content = RichTextField(verbose_name="Content", null=True, blank=True)
    
    def __str__(self):
        return self.content
    
class EmploymentAndUnemployment(models.Model):
    content = RichTextField(verbose_name="Content", null=True, blank=True)
    
    def __str__(self):
        return self.content
    
