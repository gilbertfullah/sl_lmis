from django import forms
from .models import IndustrialRelation
from django.core.validators import RegexValidator
from django.db import transaction

GENDER_CHOICES = [
        ('', 'Select a gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
COMPLAINT_NATURE = [
        ('', 'Select a complaint nature'),
        ('Termination', 'Termination'),
        ('Dismissal', 'Dismissal'),
        ('Redundancy', 'Redundancy'),
        ('Resignation', 'Resignation'),
        ('Occupational Accident', 'Occupational Accident'),
        ('Other', 'Other'),
    ]
    
STATUS = [
        ('', 'Select a status complaint'),
        ('Resolved', 'Resolved'),
        ('Pending', 'Pending'),
        ('Industrial Court', 'Referred to Industrial Court'),
    ]

class IndustrialRelationsForm(forms.ModelForm):
    case_number = forms.CharField(label="Case Number", min_length=3, validators= [RegexValidator(r'^[a-zA-Z0-9\s]*$',
                                 message="Only letter and numbers are allowed!")], required=True,
                                 widget=forms.TextInput(attrs={'placeholder':'Case Number', 
                                                               'style':'font-size: 13px; text-transform: capitalize'}))
    
    complainant_name = forms.CharField(label="Complainant Name", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$',
                                 message="Only letter is allowed!")], required=True,
                                 widget=forms.TextInput(attrs={'placeholder':'Complainant Name', 
                                                               'style':'font-size: 13px; text-transform: capitalize'}))
    
    complaint_gender = forms.ChoiceField(label="Complainant Gender", widget=forms.Select(attrs={"class":"form-control"}), choices=GENDER_CHOICES)
    
    employer_name = forms.CharField(label="Employer Name", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$',
                                 message="Only letter is allowed!")], required=True,
                                 widget=forms.TextInput(attrs={'placeholder':'Employer Name', 
                                                               'style':'font-size: 13px; text-transform: capitalize'}))
    
    investigating_officer_name = forms.CharField(label="Name of Investigating Officer", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$',
                                 message="Only letter is allowed!")], required=True,
                                 widget=forms.TextInput(attrs={'placeholder':'Name of Investigating Officer', 
                                                               'style':'font-size: 13px; text-transform: capitalize'}))
    
    complaint_nature = forms.ChoiceField(label="Nature of Complaint", widget=forms.Select(attrs={"class":"form-control"}), choices=COMPLAINT_NATURE)
    
    date = forms.DateField(label="Date", required=True, widget=forms.DateInput(attrs={'class': 'form-control datepicker-input'}))
    
    complaint_status = forms.ChoiceField(label="Status of Complaint", widget=forms.Select(attrs={"class":"form-control"}), choices=STATUS)
    
    settlement_fee = forms.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, required=False)
    
    class Meta:
        model = IndustrialRelation
        fields = ('case_number','complainant_name', 'complaint_gender', 'date', 'employer_name', 'complaint_nature', 'investigating_officer_name', 
                  'complaint_status', 'settlement_fee',)