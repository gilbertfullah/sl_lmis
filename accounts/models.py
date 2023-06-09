from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.utils import timezone


class User(AbstractUser):
    is_jobseeker = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_government = models.BooleanField(default=False)
    
class JobSeeker(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Disapproved','Disapproved')
    )
    
    CHOICES = (
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Internship', 'Internship'),
        ('Freelance', 'Freelance')
)

    
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20)
    profile_pic = models.FileField(null=True, blank=True)
    #country = CountryField(null=True, blank=True)
    location = models.CharField(max_length=100)
    education_level = models.CharField(max_length=200)
    course_training = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    grad_year = models.CharField(max_length=4)
    resume = models.FileField(null=True, blank=True)
    looking_for = models.CharField(max_length=30)
    status = models.CharField(max_length=50, null=True, choices=STATUS, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2', 'gender', 'age', 'education_level', 'course_training', 
                       'profession', 'grad_year', 'looking_for']
    
    def __str__(self):
        return self.username
    
    #Concatenate first and last name
    def name(obj):
        return "%s %s" % (obj.first_name, obj.last_name)
    
class Skill(models.Model):
    skill = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name='skills', on_delete=models.CASCADE)
    
class Company(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Disapproved','Disapproved')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True, max_length=1000)
    email = models.EmailField(unique=True)
    region = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    sector = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    company_logo = models.FileField(null=True, blank=True)
    company_certificate = models.FileField()
    status = models.CharField(max_length=50, null=True, choices=STATUS, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'company_name', 'region', 'phone_number', 'sector', 'address', 'company_certificate']
   
    def __str__(self):
        return self.company_name
    
class Government(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Disapproved','Disapproved')
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    government_institution_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True, max_length=1000)
    email = models.EmailField(unique=True)
    region = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    sector = models.CharField(max_length=100)
    logo = models.FileField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.government_institution_name


