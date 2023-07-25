from django.db import models
from accounts.models import Company
from django.utils import timezone
from django.conf import settings
User = settings.AUTH_USER_MODEL
from ckeditor.fields import RichTextField

#from ..accounts.models import Company

class Job(models.Model):
    CONTRACT_CHOICES = [
        ('', 'Select a contract type'),
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
        ('Freelance', 'Freelance')
    ]
    
    EXP_CHOICES = [
        ('', 'Select an experience level'),
        ('No experience', 'No experience'),
        ('Less than 1 year', 'Less than 1 year'),
        ('1 - 2 years', '1 - 2 years'),
        ('2 - 5 years', '2 - 5 years'),
        ('5 - 10 years', '5 - 10 years'),
        ('More than 10 years', 'More than 10 years'),
    ]
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Job Title", max_length=200)
    description = RichTextField(verbose_name="Job Description", null=True, blank=True)
    location = models.CharField(verbose_name="Location", max_length=200, default="Western Area")
    contract = models.CharField(verbose_name="Contract-Type", max_length=100, choices=CONTRACT_CHOICES)
    sector = models.CharField(verbose_name="Sector", max_length=200, default="Accounting")
    salary = models.CharField(verbose_name="Salary", max_length=200, null=True, blank=True)
    expiration_date = models.DateField(verbose_name="Expiration Date")
    published_date = models.DateField(verbose_name="Published Date", default=timezone.now)
    experience = models.CharField(verbose_name="Working Experience", max_length=200, choices=EXP_CHOICES)
    qualification = models.CharField(verbose_name="Qualification", max_length=200, default="Bachelors")
    requirements = RichTextField(verbose_name="Requirement", null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    updated = models.DateField(auto_now=True)
    created_at = models.DateField(default=timezone.now)
    
    class Meta:
        ordering = ['-updated', '-created_at']
    
    def __str__(self):
        return self.title




class SavedJobs(models.Model):
    job = models.ForeignKey(Job, related_name='saved_job', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='saved', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.title
    

class AppliedJobs(models.Model):
    job = models.ForeignKey(Job, related_name='applied_job', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='applied_user', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.title
    
class Applicants(models.Model):
    job = models.ForeignKey(Job, related_name='applicants', on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, related_name='applied', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant
    
class Selected(models.Model):
    job = models.ForeignKey(Job, related_name='select_job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, related_name='select_applicant', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant
    
class Employer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    company_size = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField()