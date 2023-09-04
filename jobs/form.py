from django import forms
from .models import Job
from email import message
from django.core.validators import RegexValidator
from django.db import transaction
from ckeditor.widgets import CKEditorWidget


CONTRACT_CHOICES = (
        ('', 'Select a contract type'),
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Internship', 'Internship'),
        ('Freelance', 'Freelance'),
        ('Remote', 'Remote')
)

EDUCATION_LEVEL = (
        ('', 'Select a qualification'),
        ('High School Certificate', 'High School Certificate'),
        ('Certificate', 'Certificate'),
        ('Diploma', 'Diploma'),
        ('College', 'College'),
        ('Bachelor Degree', 'Bachelor Degree'),
        ('Master Degree', 'Master Degree'),
        ('Doctrate Degree', 'Doctrate(Ph.D) Degree'),
    )

EXPERIENCE_LEVEL = (
        ('', 'Select an experience level'),
        ('No experience', 'No experience'),
        ('Less than 1 year', 'Less than 1 year'),
        ('1 - 2 years', '1 - 2 years'),
        ('2 - 5 years', '2 - 5 years'),
        ('5 - 10 years', '5 - 10 years'),
        ('More than 10 years', 'More than 10 years'),
    )

LOCATION = (
        ('', 'Select a location'),
        ('Bo', 'Bo'),
        ('Bomabili', 'Bomabili'),
        ('Bonthe', 'Bonthe'),
        ('Falaba', 'Falaba'),
        ('Kailahun', 'Kailahun'),
        ('Kambia', 'Kambia'),
        ('Karene', 'Karene'),
        ('Kenema', 'Kenema'),
        ('Koinadugu', 'Koinadugu'),
        ('Kono', 'Kono'),
        ('Moyamba', 'Moyamba'),
        ('Port Loko', 'Port Loko'),
        ('Pujehun', 'Pujehun'),
        ('Tonkolili', 'Tonkolili'),
        ('Western Rural', 'Western Rural'),
        ('Western Urban', 'Western Urban'),
        ('International', 'International'),
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
        ('Transport and Logistics', 'Transport and Logistics'),
        ('Tourism, Hotel business and Catering', 'Tourism, Hotel business and Catering'),
        ('Audit', 'Audit'),
        ('HR', 'HR'),
        ('ICT/Telecommunication', 'IT, Software engineering, Internet, Telecommunication'),
        ('Legal', 'Legal'),
        ('Management', 'Management'),
        ('Marketing, Communication, Media', 'Marketing, Communication, Media'),
        ('R&D, Project Management', 'R&D, Project Management'),
        ('Sales', 'Sales'),
        ('Services', 'Services'),
        ('Public buildings and Works profession', 'Public buildings and Works profession'),
        ('Purchases', 'Purchases'),
        ('Airport and Shipping Services', 'Airport and Shipping Services'),
        ('Accounting/Finance', 'Banking, Insurance, Finances'),
        ('Associative activities', 'Associative activities'),
        ('Call centers, Hotlines', 'Call centers, Hotlines'),
        ('Cleaning, Security, Surveillance', 'Cleaning, Security, Surveillance'),
        ('Edition, Printing', 'Edition, Printing'),
        ('Education, Training', 'Education, Training'),
        ('Electric, Electronics, Optical and Precision equipments', 'Electric, Electronics, Optical and Precision equipments'),
        ('Engineering', 'Engineering'),
        ('Procurement', 'Procurement'),
        ('Public Health', 'Public Health'),
        ('Project Management', 'Project Management'),
        ('Driver', 'Driver'),
        ('Business Administration', 'Business Administration'),
        ('Environment, Recycling', 'Environment, Recycling'),
        ('Event, Receptionist', 'Event, Receptionist'),
        ('Food processing', 'Food processing'),
        ('Healthcare', 'Health, Pharmacy, Hospital, Medical equipments'),
        ('Import, Export', 'Import, Export'),
        ('Cosmetics', 'Cosmetics'),
        ('Sports', 'Sports'),
        ('Others', 'Others'),
    )

class JobForm(forms.ModelForm):
    employer = forms.CharField(label="Company", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], required=True,
                                widget=forms.TextInput(attrs={'placeholder':'Company', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    title = forms.CharField(label="Job Title", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], 
                            required=True, widget=forms.TextInput(attrs={'placeholder':'Job title', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    location = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=LOCATION)
    experience = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=EXPERIENCE_LEVEL)
    sector = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=SECTOR)
    contract = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=CONTRACT_CHOICES)
    qualification = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=EDUCATION_LEVEL)
    description = forms.CharField(label="Job description", min_length=50, required=True, widget=CKEditorWidget())
    skills = forms.CharField(label="Professional Skills", min_length=50, required=True, widget=CKEditorWidget())
    requirements = forms.CharField(label="Job requirements", min_length=50, required=True, widget=CKEditorWidget())
    expiration_date = forms.DateField(label="Job Expiration Date", required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control datepicker-input'}))
    published_date = forms.DateField(label="Job Expiration Date", required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control datepicker-input'}))
    image = forms.FileField(label="Upload company logo", required=False, widget=forms.ClearableFileInput(attrs={'style':'font-size: 13px'}))
    
    class Meta:
        model = Job
        fields = ['title', 'location', 'experience', 'description','sector', 'contract', 'qualification', 
                'requirements', 'expiration_date', 'published_date', 'image', 'skills']


class JobUpdateForm(forms.ModelForm):
    company = forms.CharField(label="Company", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$',
                                 message="Only letter is allowed!")], required=True,
                                 widget=forms.TextInput(attrs={'placeholder':'Company', 
                                                               'style':'font-size: 13px; text-transform: capitalize'}))
    
    title = forms.CharField(label="Job Title", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$',
                                 message="Only letter is allowed!")], required=True,
                                 widget=forms.TextInput(attrs={'placeholder':'Job title', 
                                                               'style':'font-size: 13px; text-transform: capitalize'}))
    salary = forms.CharField(label="Salary", min_length=3, validators= [RegexValidator(r'^[a-zA-Z0-9-\s]*$',
                                 message="Only letter is allowed!")], required=False,
                                 widget=forms.TextInput(attrs={'placeholder':'Salary', 
                                                               'style':'font-size: 13px; text-transform: capitalize'}))
    location = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=LOCATION)
    experience = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=EXPERIENCE_LEVEL)
    sector = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=SECTOR)
    contract = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=CONTRACT_CHOICES)
    qualification = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=EDUCATION_LEVEL)
    description = forms.CharField(label="Job description", min_length=50, required=True,
                                 widget=forms.Textarea(attrs={'placeholder':'Write a brief job description', 
                                                               'style':'font-size: 13px', 'rows':4}))
    requirements = forms.CharField(label="Job requirements", min_length=50, required=True,
                                 widget=forms.Textarea(attrs={'placeholder':'Write a brief job requirements', 
                                                               'style':'font-size: 13px', 'rows':4}))
    expiration_date = forms.DateField(label="Job Expiration Date", required=False, widget=forms.DateInput(attrs={'class': 'form-control datepicker-input'}))
    logo = forms.FileField(label="Upload company logo", required=False, widget=forms.ClearableFileInput(attrs={'style':'font-size: 13px'}))
    
    class Meta:
        model = Job
        fields = ('company', 'title', 'salary', 'location', 'experience', 'description', 'sector', 
                  'contract', 'qualification', 'requirements', 'expiration_date', 'logo')
        help_texts = {
            'skills_req': 'Enter all the skills required each separated by commas.',
            'link': 'If you want candidates to apply on your company website rather than on our website, please provide the link where candidates can apply. Otherwise, please leave it blank or candidates would not be able to apply directly!',
        }

class JobSearchForm(forms.Form):
    title = forms.CharField(max_length=250, required=False,)
    location = forms.ChoiceField(choices=LOCATION, required=False,)
    

class JobApplicationForm(forms.Form):
    first_name = forms.CharField(label="First Name", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], error_messages={'required':'First name cannot be empty'}, required=True,
                                widget=forms.TextInput(attrs={'placeholder':'First name', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    last_name = forms.CharField(label="Last Name", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], error_messages={'required':'Last name cannot be empty'}, required=True,
                                widget=forms.TextInput(attrs={'placeholder':'Last name', 'style':'font-size: 13px; text-transform: capitalize'}))
    email = forms.CharField(label="Email", min_length=8, required=True, error_messages={'required':'Email cannot be empty'}, widget=forms.TextInput(attrs={'placeholder':'Email',
                            'style':'font-size: 13px; text-transform: lowercase'}))
    phone_number = forms.CharField(label="Phone Number", required=True, error_messages={'required':'Phone number cannot be empty'},
                                widget=forms.TextInput(attrs={'style':'font-size: 13px', 'placeholder':'Phone Number'}))
    resume = forms.FileField(label="Upload your CV", required=False, widget=forms.ClearableFileInput(attrs={'style':'font-size: 13px'}))
    title = forms.CharField(label="Job Title", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], 
                            required=True, widget=forms.TextInput(attrs={'placeholder':'Job title', 'style':'font-size: 13px; text-transform: capitalize'}))

    def __init__(self, *args, **kwargs):
        initial_data = kwargs.pop('initial_data', {})
        super().__init__(*args, **kwargs)
        self.initial.update(initial_data)