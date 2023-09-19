from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, JobSeeker, Employer, Government
from email import message
from django.core.validators import RegexValidator, FileExtensionValidator
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError
from ckeditor.widgets import CKEditorWidget
from phonenumber_field.formfields import PhoneNumberField
#from phonenumber_field.widgets import PhoneNumberPrefixWidget

GENDER = (
        ('', 'Select a gender'),
        ('Male', 'Male'),
        ('Female','Female')
    )

EDUCATION_LEVEL = (
        ('', 'Select an education level'),
        ('High School', 'High School'),
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
        ('1 year', '1 year'),
        ('2 years', '2 years'),
        ('3 years', '3 years'),
        ('4 years', '4 years'),
        ('5 years', '5 years'),
        ('10 years', '10 years'),
        ('10+ years', '10+ years'),
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

CHOICES = (
        ('', 'Select type of job'),
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
        ('Apprenticeship', 'Apprenticeship'),
        ('Freelance', 'Freelance'),
        ('Remote', 'Remote')
)

DISTRICT = (
        ('', 'Select a location'),
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

EMPLOYMENT_STATUS = (
    ('', 'Select employment status'),
    ('Employed', 'Employed'),
    ('Self-Employed', 'Self-Employed'),
    ('Unemployed', 'Unemployed'),
    ('Student', 'Student'),
    ('Retired', 'Retired'),
)



def validate_file_size(value):
    MAX_FILE_SIZE = 5 * 1024 * 1024
    if value.size > MAX_FILE_SIZE:
        raise forms.ValidationError('File size cannot exceed 5MB.')

class JobSeekerRegisterForm(UserCreationForm):
    username = forms.CharField(label="Username", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], error_messages={'required':'Username cannot be empty'}, required=True,
                                widget=forms.TextInput(attrs={'placeholder':'Username', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    password1 = forms.CharField(label="Password", min_length=3, required=True, error_messages={'required':'Password cannot be empty'},
                                widget=forms.PasswordInput(attrs={'placeholder':'Password', 'style':'font-size: 13px;'}))
    
    password2 = forms.CharField(label="Password confirmation", min_length=3, required=True, error_messages={'required':'Confirm password cannot be empty'},
                                widget=forms.PasswordInput(attrs={'placeholder':'Password confirmation', 'style':'font-size: 13px;'}))
    
    first_name = forms.CharField(label="First Name", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], error_messages={'required':'First name cannot be empty'}, required=True,
                                widget=forms.TextInput(attrs={'placeholder':'First name', 'autofocus': 'autofocus', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    last_name = forms.CharField(label="Last Name", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], error_messages={'required':'Last name cannot be empty'}, required=True,
                                widget=forms.TextInput(attrs={'placeholder':'Last name', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    profession = forms.CharField(label="Profession", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], error_messages={'required':'Profession cannot be empty'}, required=False,
                                widget=forms.TextInput(attrs={'placeholder':'Example: Accountant', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    qualification = forms.CharField(label="Qualification", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], error_messages={'required':'Qualification cannot be empty'}, required=True,
                                widget=forms.TextInput(attrs={'placeholder':'Example: Accountant', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    email = forms.CharField(label="Email", min_length=8, required=True, error_messages={'required':'Email cannot be empty'}, widget=forms.TextInput(attrs={'placeholder':'Email',
                            'style':'font-size: 13px; text-transform: lowercase'}))
    
    gender = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=GENDER, error_messages={'required':'Gender cannot be empty'},)
    
    education_level = forms.ChoiceField(label="Highest level of education", widget=forms.Select(attrs={"class":"form-control"}), choices=EDUCATION_LEVEL, error_messages={'required':'Education level cannot be empty'},)

    district = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=DISTRICT, error_messages={'required':'District cannot be empty'},)
    
    age = forms.CharField(label="Age", min_length=2, validators=[RegexValidator(r'^[0-9]*$', message="Only number is allowed!")], error_messages={'required':'Age cannot be empty'},
                        widget=forms.TextInput(attrs={'placeholder':'Your Age', 'style':'font-size: 13px'}))
    
    phone_number = PhoneNumberField(label="Phone Number", required=True, error_messages={'required':'Phone number cannot be empty'},
                                widget=forms.TextInput(attrs={'class':" form-control", 'style':'font-size: 13px', 'placeholder':'Example: +23276901488'}))
    
    about = forms.CharField(widget=CKEditorWidget())
    
    profile_pic = forms.FileField(label="Upload your profile picture", error_messages={'required':'Profile Pic cannot be empty'}, help_text="Allowed file type: JPG, JPEG, PNG. Maximum file size: 5MB.",
                                widget=forms.ClearableFileInput(attrs={'class':'form-control', 'style':'font-size: 13px', 'accept': 'image/png, image/jpeg, image/jpg'}))

    grad_year = forms.CharField(label="Graduation year", min_length=2, required=True, validators=[RegexValidator(r'^[0-9]*$', message="Only number is allowed!")],
                                error_messages={'required':'Graduation year cannot be empty'}, widget=forms.TextInput(attrs={'style':'font-size: 13px', 'placeholder':'Graduation Year'}))
    
    resume = forms.FileField(label="Upload your CV", error_messages={'required':'Resume cannot be empty'}, help_text="Allowed file type: PDF. Maximum file size: 5MB.",
                            widget=forms.ClearableFileInput(attrs={'class':'form-control','style':'font-size: 13px', 'accept': 'application/pdf'}))
    
    looking_for = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=CHOICES, error_messages={'required':'Looking for cannot be empty'},)
    
    employment_status = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=EMPLOYMENT_STATUS, error_messages={'required':'Employment status cannot be empty'},)
    
    facebook = forms.URLField(max_length=150, min_length=3, required=False, widget=forms.TextInput(attrs={'placeholder':'Enter your facebook account link', 'style':'font-size: 13px;'}))
    
    linkedin = forms.URLField(max_length=150, min_length=3, required=False, widget=forms.TextInput(attrs={'placeholder':'Enter your linkedin account link', 'style':'font-size: 13px;'}))
    
    twitter = forms.URLField(max_length=150, min_length=3, required=False, widget=forms.TextInput(attrs={'placeholder':'Enter your twitter account link', 'style':'font-size: 13px;'}))
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        for obj in JobSeeker.objects.all():
            if obj.email == email:
                raise forms.ValidationError("Denied! " + email + " is already registered.")
        return email

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'looking_for', 'resume', 'grad_year', 'about', 'facebook',
                'age', 'phone_number', 'district', 'gender', 'education_level', 'profile_pic', 'profession', 'employment_status', 'linkedin', 'twitter')
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_jobseeker = True
        user.username = self.cleaned_data.get('username')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.password1 = self.cleaned_data.get('password1')
        user.password2 = self.cleaned_data.get('password2')
        user.save()
        jobseeker = JobSeeker.objects.create(user=user)
        jobseeker.username = self.cleaned_data.get('username')
        jobseeker.first_name = self.cleaned_data.get('first_name')
        jobseeker.last_name = self.cleaned_data.get('last_name')
        jobseeker.email = self.cleaned_data.get('email')
        jobseeker.password1 = self.cleaned_data.get('password1')
        jobseeker.password2 = self.cleaned_data.get('password2')
        jobseeker.age = self.cleaned_data.get('age')
        jobseeker.phone_number = self.cleaned_data.get('phone_number')
        jobseeker.district = self.cleaned_data.get('district')
        jobseeker.gender = self.cleaned_data.get('gender')
        jobseeker.education_level = self.cleaned_data.get('education_level')
        jobseeker.about = self.cleaned_data.get('about')
        jobseeker.profile_pic = self.cleaned_data.get('profile_pic')
        jobseeker.looking_for = self.cleaned_data.get('looking_for')
        jobseeker.resume = self.cleaned_data.get('resume')
        jobseeker.grad_year = self.cleaned_data.get('grad_year')
        jobseeker.profession = self.cleaned_data.get('profession')
        jobseeker.employment_status = self.cleaned_data.get('employment_status')
        jobseeker.facebook = self.cleaned_data.get('facebook')
        jobseeker.twitter = self.cleaned_data.get('twitter')
        jobseeker.linkedin = self.cleaned_data.get('linkedin')
        jobseeker.save()
        return user

class CompanyRegisterForm(UserCreationForm):
    username = forms.CharField(label="Username", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], error_messages={'required':'Username cannot be empty'}, required=True,
                                widget=forms.TextInput(attrs={'placeholder':'Username', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    company_name = forms.CharField(label="Company Name", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], error_messages={'required':'Company name cannot be empty'}, required=True,
                                widget=forms.TextInput(attrs={'placeholder':'Company name', 'autofocus': 'autofocus', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    description = forms.CharField(widget=CKEditorWidget())
    
    password1 = forms.CharField(label="Password", min_length=3, required=True, error_messages={'required':'Password cannot be empty'},
                                widget=forms.PasswordInput(attrs={'placeholder':'Password', 'style':'font-size: 13px;'}))
    
    password2 = forms.CharField(label="Password confirmation", min_length=3, required=True, error_messages={'required':'Confirm password cannot be empty'},
                                widget=forms.PasswordInput(attrs={'placeholder':'Password confirmation', 'style':'font-size: 13px;'}))
    
    email = forms.CharField(label="Email", min_length=8, required=True, error_messages={'required':'Email cannot be empty'},
                            widget=forms.TextInput(attrs={'placeholder':'Email','style':'font-size: 13px; text-transform: lowercase'}))
    
    phone_number = PhoneNumberField(label="Phone Number", required=True, error_messages={'required':'Phone number cannot be empty'},
                                widget=forms.TextInput(attrs={'class':" form-control", 'style':'font-size: 13px', 'placeholder':'Example: +23276901488'}), help_text="Please enter your phone number")
    
    district = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=DISTRICT, error_messages={'required':'District cannot be empty'},)
    
    sector = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=SECTOR, error_messages={'required':'Sector cannot be empty'},)
    
    address = forms.CharField(label="Company Address", min_length=3, validators= [RegexValidator(r'^[a-zA-Z0-9-,\s]*$',
                                message="Only letters and numbers is allowed!")], error_messages={'required':'Address cannot be empty'}, required=True,
                                widget=forms.TextInput(attrs={'placeholder':'Company address', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    company_certificate = forms.FileField(label="Upload company registration certificate", required=True, error_messages={'required':'Company certificate cannot be empty'}, validators=[FileExtensionValidator(allowed_extensions=['pdf']), validate_file_size],
                                        help_text="Allowed file type: PDF. Maximum file size: 5MB.",
                                        widget=forms.ClearableFileInput(attrs={'class':'form-control','style':'font-size: 13px', 'accept': 'application/pdf'}))
    
    company_logo = forms.FileField(label="Upload company logo", error_messages={'required':'Company logo cannot be empty'}, help_text="Allowed file type: JPG, JPEG, PNG. Maximum file size: 5MB.",
                                widget=forms.ClearableFileInput(attrs={'class':'form-control', 'style':'font-size: 13px', 'accept': 'image/png, image/jpeg, image/jpg'}))
    
    company_size = forms.CharField(label="Company size", min_length=1, required=False, validators= [RegexValidator(r'^[0-9\s]*$',
                                message="Only number is allowed!")], widget=forms.TextInput(attrs={'placeholder':'30', 'style':'font-size: 13px;'}))
    
    website = forms.URLField(max_length=150, min_length=3, required=True, widget=forms.TextInput(attrs={'placeholder':'Example: learnable.com', 'style':'font-size: 13px;'}))
    
    facebook = forms.URLField(max_length=150, min_length=3, required=False, widget=forms.TextInput(attrs={'placeholder':'Enter your facebook account link', 'style':'font-size: 13px;'}))
    
    linkedin = forms.URLField(max_length=150, min_length=3, required=False, widget=forms.TextInput(attrs={'placeholder':'Enter your linkedin account link', 'style':'font-size: 13px;'}))
    
    twitter = forms.URLField(max_length=150, min_length=3, required=False, widget=forms.TextInput(attrs={'placeholder':'Enter your twitter account link', 'style':'font-size: 13px;'}))
    

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('company_name', 'username', 'email', 'password1', 'password2', 'description', 'phone_number', 'district', 
                'sector', 'company_certificate', 'company_logo', 'address', 'company_size', 'website', 'facebook', 'twitter', 'linkedin')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        for obj in Employer.objects.all():
            if obj.email == email:
                raise forms.ValidationError("Denied! " + email + " is already registered.")
        return email

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.password1 = self.cleaned_data.get('password1')
        user.password2 = self.cleaned_data.get('password2')
        user.save()
        company = Employer.objects.create(user=user)
        company.username = self.cleaned_data.get('username')
        company.company_name = self.cleaned_data.get('company_name')
        company.email = self.cleaned_data.get('email')
        company.password1 = self.cleaned_data.get('password1')
        company.password2 = self.cleaned_data.get('password2')
        company.description = self.cleaned_data.get('description')
        company.phone_number = self.cleaned_data.get('phone_number')
        company.district = self.cleaned_data.get('district') 
        company.sector = self.cleaned_data.get('sector')
        company.company_certificate = self.cleaned_data.get('company_certificate')
        company.company_logo = self.cleaned_data.get('company_logo')
        company.address = self.cleaned_data.get('address')
        company.company_size = self.cleaned_data.get('company_size')
        company.website = self.cleaned_data.get('website')
        company.facebook = self.cleaned_data.get('facebook')
        company.twitter = self.cleaned_data.get('twitter')
        company.linkedin = self.cleaned_data.get('linkedin')
        company.save()
        return user
    
class GovernmentRegisterForm(UserCreationForm):
    username = forms.CharField(label="Username", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], required=True,
                                widget=forms.TextInput(attrs={'placeholder':'Username', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    government_institution_name = forms.CharField(label="Ministry Name", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], required=True,
                                 widget=forms.TextInput(attrs={'placeholder':'Ministry name', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    email = forms.CharField(label="Email", min_length=8, required=True, widget=forms.TextInput(attrs={'placeholder':'Email', 'style':'font-size: 13px; text-transform: lowercase'}))
    
    password1 = forms.CharField(label="Password", min_length=3, required=True, widget=forms.PasswordInput(attrs={'placeholder':'Password', 'style':'font-size: 13px;'}))
    
    password2 = forms.CharField(label="Password confirmation", min_length=3, required=True, widget=forms.PasswordInput(attrs={'placeholder':'Password confirmation', 'style':'font-size: 13px;'}))
    
    description = forms.CharField(label="Ministry description", min_length=50, required=True,
                                widget=CKEditorWidget())
    
    phone_number = forms.CharField(label="Phone Number", required=True, widget=forms.TextInput(attrs={'style':'font-size: 13px', 
                                    'placeholder':'Phone Number'}))
    
    district = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=DISTRICT)
    
    sector = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=SECTOR)
    
    logo = forms.FileField(label="Upload institution logo", required=False, widget=forms.ClearableFileInput(attrs={'style':'font-size: 13px'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('government_institution_name', 'username', 'email', 'password1', 'password2', 'description', 'phone_number', 
                  'district', 'sector', 'logo',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_government = True
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.password1 = self.cleaned_data.get('password1')
        user.password2 = self.cleaned_data.get('password2')
        user.save()
        government = Government.objects.create(user=user)
        government.username = self.cleaned_data.get('username')
        government.government_institution_name = self.cleaned_data.get('government_institution_name')
        government.email = self.cleaned_data.get('email')
        government.password1 = self.cleaned_data.get('password1')
        government.password2 = self.cleaned_data.get('password2')
        government.description = self.cleaned_data.get('description')
        government.phone_number = self.cleaned_data.get('phone_number')
        government.district = self.cleaned_data.get('district')
        government.sector = self.cleaned_data.get('sector')
        government.logo = self.cleaned_data.get('logo')
        government.save()
        return user
    
    
def login_form(request):
    username = forms.CharField(label="Username", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$',
                                message="Only letter is allowed!")], error_messages={'required':'Username cannot be empty'}, required=True,
                                widget=forms.TextInput(attrs={'placeholder':'Username', 'autofocus': 'autofocus', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    password1 = forms.CharField(label="Password", min_length=3, required=True, error_messages={'required':'Password cannot be empty'},
                                widget=forms.PasswordInput(attrs={'placeholder':'Password', 'style':'font-size: 13px;'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1')
    

class JobseekerProfileForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = "__all__"

