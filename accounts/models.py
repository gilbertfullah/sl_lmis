from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import magic

DISTRICT = (
        ('', 'Select a district'),
        ('Bo', 'Bo'),
        ('Bonthe', 'Bonthe'),
        ('Bombali', 'Bombali'),
        ('Falaba', 'Falaba'),
        ('Kailahun', 'Kailahun'),
        ('Kambia', 'Kambia'),
        ('Kenema', 'Kenema'),
        ('Koinadugu', 'Koinadugu'),
        ('Karene', 'Karene'),
        ('Kono', 'Kono'),
        ('Moyamba', 'Moyamba'),
        ('Port Loko', 'Port Loko'),
        ('Pujehun', 'Pujehun'),
        ('Tonkolili', 'Tonkolili'),
        ('Western Rural', 'Western Rural'),
        ('Western Urban', 'Western Urban'),
        ('International', 'International'),
)

CHOICES = (
        ('', 'Select a job type'),
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
        ('Freelance', 'Freelance'),
        ('Apprenticeship', 'Apprenticeship'),
        ('Remote', 'Remote')
)

STATUS = (
    ('', 'Select a status'),
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected')
)

EMPLOYMENT_STATUS = (
    ('', 'Select employment staus'),
    ('Employed', 'Employed'),
    ('Self-Employed', 'Self-Employed'),
    ('Unemployed', 'Unemployed'),
    ('Student', 'Student'),
    ('Retired', 'Retired'),
)

SECTOR = (
        ('', 'Select a category'),
        ('Agriculture, Fishing, Aquaculture', 'Agriculture, Fishing, Aquaculture'),
        ('Trade and Investment', 'Trade and Investment'),
        ('Wholesale and retail trade', 'Wholesale and retail trade'),
        ('Mining, Chemistry, Petrochemistry, raw materials', 'Mining, Chemistry, Petrochemistry, raw materials'),
        ('Government Services', 'Government Services'),
        ('Manufacturing and handicrafts', 'Manufacturing and handicrafts'),
        ('Construction', 'Construction'),
        ('Electricity and water', 'Electricity and water'),
        ('Telecommunications', 'Telecommunications'),
        ('Transport and Logistics', 'Transport and Logistics'),
        ('Tourism, Hotel business and Catering', 'Tourism, Hotel business and Catering'),
        ('Audit, Advice, Accounting', 'Audit, Advice, Accounting'),
        ('Health, Social Professions', 'Health, Social Professions'),
        ('HR', 'HR'),
        ('IT, Software engineering, Internet', 'IT, Software engineering, Internet'),
        ('Legal', 'Legal'),
        ('Management', 'Management'),
        ('Marketing, Communication, Media', 'Marketing, Communication, Media'),
        ('R&D, Project Management', 'R&D, Project Management'),
        ('Sales', 'Sales'),
        ('Services', 'Services'),
        ('Public buildings and Works profession', 'Public buildings and Works profession'),
        ('Purchases', 'Purchases'),
        ('Airport and Shipping Services', 'Airport and Shipping Services'),
        ('Banking, Insurance, Finance', 'Airport and Shipping Services'),
        ('Associative activities', 'Associative activities'),
        ('Call centers, Hotlines', 'Call centers, Hotlines'),
        ('Cleaning, Security, Surveillance', 'Cleaning, Security, Surveillance'),
        ('Edition, Printing', 'Edition, Printing'),
        ('Education, Training', 'Education, Training'),
        ('Electric, Electronics, Optical and Precision equipments', 'Electric, Electronics, Optical and Precision equipments'),
        ('Engineering, Development studies', 'Engineering, Development studies'),
        ('Environment, Recycling', 'Environment, Recycling'),
        ('Event, Receptionist', 'Event, Receptionist'),
        ('Food processing', 'Food processing'),
        ('Health, Pharmacy, Hospital, Medical equipments', 'Health, Pharmacy, Hospital, Medical equipments'),
        ('Import, Export', 'Import, Export'),
        ('Cosmetics', 'Cosmetics'),
        ('Sports, Cultural and Social action', 'Sports, Cultural and Social action'),
        ('Others', 'Others'),
    )

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

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

class User(AbstractUser):
    is_jobseeker = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_government = models.BooleanField(default=False)
    

class JobSeeker(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    email = models.EmailField(max_length=50)
    phone_number = PhoneNumberField(max_length=50, unique=True, help_text="")
    about = RichTextField(max_length=1000)
    profile_pic = models.FileField(upload_to=user_directory_path, validators=[image_ex_validator, validate_image_type, validate_file_size])
    district = models.CharField(max_length=250, choices=DISTRICT)
    education_level = models.CharField(max_length=200)
    profession = models.CharField(max_length=200, blank=True, null=True)
    qualification = models.CharField(max_length=250)
    grad_year = models.CharField(max_length=4)
    resume = models.FileField(upload_to='resumes/', validators=[file_ex_validator, validate_file_mimetype, validate_file_size])
    looking_for = models.CharField(max_length=30)
    employment_status = models.CharField(max_length=250, choices=EMPLOYMENT_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2', 'gender', 'age', 'about', 'education_level', 
                    'profession', 'grad_year', 'looking_for', 'location', 'qualification', 'employment_status']
    
    class Meta:
        verbose_name_plural = "JobSeekers"
        
    def jobseeker_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.profile_pic.url))
    
    def __str__(self):
        return self.username
    
    #Concatenate first and last name
    def name(obj):
        return "%s %s" % (obj.first_name, obj.last_name)


    
class Employer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    company_name = models.CharField(max_length=200)
    description = RichTextField(null=True, blank=True, max_length=1000)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=250)
    phone_number = PhoneNumberField(max_length=50)
    district = models.CharField(max_length=250, choices=DISTRICT)
    company_logo = models.FileField(upload_to=user_directory_path, validators=[image_ex_validator, validate_image_type, validate_file_size])
    company_certificate = models.FileField()
    company_size = models.CharField(max_length=255, null=True, blank=True)
    website = models.URLField()
    sector = models.CharField(max_length=250, choices=SECTOR)
    status = models.CharField(choices=STATUS, max_length=50, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'company_name', 'district', 'phone_number', 'sector', 'address', 'company_certificate']
   
    class Meta:
        verbose_name_plural = "Employers"
        
    def employer_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.company_logo.url))
    
    def __str__(self):
        return self.company_name
    
class Government(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    institution_name = models.CharField(max_length=200)
    description = RichTextField(null=True, blank=True, max_length=1000)
    email = models.EmailField(unique=True)
    district = models.CharField(max_length=250, choices=DISTRICT)
    phone_number = models.CharField(max_length=50)
    sector = models.CharField(max_length=250, choices=SECTOR)
    logo = models.FileField(upload_to=user_directory_path, validators=[image_ex_validator, validate_image_type, validate_file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Government"
        
    def government_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.logo.url))
   
    def __str__(self):
        return self.institution_name

class ProfileView(models.Model):
    viewer = models.ForeignKey(User, on_delete=models.CASCADE)
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('viewer', 'jobseeker')