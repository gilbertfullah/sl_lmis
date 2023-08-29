from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.utils import timezone
from ckeditor.fields import RichTextField
#from shortuuidfield import ShortUUIDField
#import shortuuid
import uuid
from django.utils.html import mark_safe


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
)

CHOICES = (
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Internship', 'Internship'),
        ('Freelance', 'Freelance')
)

STATUS = (
    ('', 'Select a status'),
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected')
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

class User(AbstractUser):
    is_jobseeker = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_government = models.BooleanField(default=False)
    
class JobSeeker(models.Model):
    #id = models.CharField(unique=True, max_length=22, primary_key=True, default=shortuuid.uuid)
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to=user_directory_path)
    district = models.CharField(max_length=250, choices=DISTRICT)
    education_level = models.CharField(max_length=200)
    profession = models.CharField(max_length=200, blank=True, null=True)
    qualification = models.CharField(max_length=250)
    grad_year = models.CharField(max_length=4)
    resume = models.FileField(null=True, blank=True)
    looking_for = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2', 'gender', 'age', 'education_level', 
                    'profession', 'grad_year', 'looking_for', 'location', 'qualification']
    
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
    #id = models.CharField(unique=True, max_length=22, primary_key=True, default=shortuuid.uuid)
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    company_name = models.CharField(max_length=200)
    description = RichTextField(null=True, blank=True, max_length=1000)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=50)
    district = models.CharField(max_length=250, choices=DISTRICT)
    company_logo = models.ImageField(upload_to=user_directory_path)
    company_certificate = models.FileField()
    company_size = models.CharField(max_length=255, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
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
    #id = models.CharField(unique=True, max_length=22, primary_key=True, default=shortuuid.uuid)
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    institution_name = models.CharField(max_length=200)
    description = RichTextField(null=True, blank=True, max_length=1000)
    email = models.EmailField(unique=True)
    district = models.CharField(max_length=250, choices=DISTRICT)
    phone_number = models.CharField(max_length=50)
    sector = models.CharField(max_length=250, choices=SECTOR)
    logo = models.ImageField(upload_to=user_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Government"
        
    def government_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.logo.url))
   
    def __str__(self):
        return self.institution_name
