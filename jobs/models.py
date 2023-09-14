from django.db import models
from accounts.models import Employer
from django.utils import timezone
from django.conf import settings
User = settings.AUTH_USER_MODEL
from ckeditor.fields import RichTextField
#from ckeditor_uploader import RichTextUploadingField
#from shortuuidfield import ShortUUIDField
import shortuuid
from shortuuid.django_fields import ShortUUIDField
import uuid
from django.utils.html import mark_safe
from taggit.managers import TaggableManager
from accounts.models import JobSeeker
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import magic
from phonenumber_field.modelfields import PhoneNumberField
    
EXP_CHOICES = (
        ('', 'Select an experience level'),
        ('No experience', 'No experience'),
        ('1 year', '1 year'),
        ('2 years', '2 years'),
        ('3 years', '3 years'),
        ('5 years', '5 years'),
        ('10 years', '10 years'),
        ('More than 10 years', 'More than 10 years'),
)

JOB_STATUS = (
    ('', 'Select a job status'),
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
    ('Closed', 'Closed')
)

QUALIFICATION = (
        ('', 'Select a qualification'),
        ('High School', 'High School'),
        ('Certificate', 'Certificate'),
        ('Diploma', 'Diploma'),
        ('College', 'College'),
        ('Bachelor Degree', 'Bachelor Degree'),
        ('Masters Degree', 'Masters Degree'),
        ('Doctrate Degree', 'Doctrate Degree'),
    )




def user_directory_path(instance, filename):
    return 'employer_{0}/{1}'.format(instance.employer.id, filename)

image_ex_validator = FileExtensionValidator(['png', 'jpeg', 'jpg'])
file_ex_validator = FileExtensionValidator(['pdf'])

def validate_image_type(file):
    accept = ['image/png', 'image/jpeg', 'image/jpg']
    file_image_type = magic.from_buffer(file.read(1024), mime=True)
    if file_image_type not in accept:
        raise ValidationError("Unsupported file type")
    
def validate_file_mimetype(file):
    accept = ['application/pdf']
    file_mimetype = magic.from_buffer(file.read(1024), mime=True)
    if file_mimetype not in accept:
        raise ValidationError("Unsupported file type")

# Define a custom file size validation function
def validate_file_size(value):
    limit = 5 * 1024 * 1024  # 5MB limit
    if value.size > limit:
        raise models.ValidationError('File size cannot exceed 5MB.')

class Sector(models.Model):
    #sid = ShortUUIDField(unique=True, max_length=20, default=shortuuid.uuid)
    #id = models.CharField(unique=True, max_length=22, primary_key=True, default=shortuuid.uuid)
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='sectors')
    
    class Meta:
        verbose_name_plural = "Sectors"
    
    def __str__(self):
        return self.title
    
class Location(models.Model):
    name = models.CharField(max_length=255)

    
    class Meta:
        verbose_name_plural = "Locations"
    
    def __str__(self):
        return self.name

class Contract(models.Model):
    name = models.CharField(max_length=255)

    
    class Meta:
        verbose_name_plural = "Contracts"
    
    def __str__(self):
        return self.name

class Job(models.Model):
    #job_id = ShortUUIDField(unique=True, length=10, max_length=20, prefix="job_", alphabet="abcdefgh12345", primary_key=True)
    #id = models.CharField(unique=True, max_length=22, primary_key=True, default=shortuuid.uuid)
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200)
    description = RichTextField(null=True, blank=True)
    skills = RichTextField(null=True, blank=True)
    experience = models.CharField(max_length=200, choices=EXP_CHOICES)
    qualification = models.CharField(max_length=200, choices=QUALIFICATION)
    requirements = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to=user_directory_path)
    tags = TaggableManager(blank=True)
    
    job_status = models.CharField(choices=JOB_STATUS, max_length=50, default="Pending")
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    expiration_date = models.DateField()
    published_date = models.DateField(default=timezone.now)
    updated = models.DateField(auto_now=True)
    created_at = models.DateField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = "Jobs"
        ordering = ['-updated', '-created_at']
    
    def __str__(self):
        return self.title


class SavedJobs(models.Model):
    job = models.ForeignKey(Job, related_name='saved_job', on_delete=models.CASCADE)
    jobseeker  = models.ForeignKey(User, related_name='saved', on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, related_name='saved_employer', on_delete=models.CASCADE)
    saved_at = models.DateTimeField(default=timezone.now) 

    class Meta:
        verbose_name_plural = "Saved Jobs"

    def __str__(self):
        return self.job.title
    

class AppliedJobs(models.Model):
    job = models.ForeignKey(Job, related_name='applied_job', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='applied_user', on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = "Applied Jobs"

    def __str__(self):
        return self.job.title


class JobApplication(models.Model):
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    jobseeker = models.ForeignKey(User, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.jobseeker.username} applied for {self.job.title}"
    


