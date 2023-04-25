from django import forms
from .models import Training
from email import message
from django.core.validators import RegexValidator


TOPIC_CHOICES = (
        ('', 'Select a topic'),
        ('Computer Science, Data Modeling & Analytics', 'Computer Science, Data Modeling & Analytics'),
        ('Biotechnology & Pharmaceutical', 'Biotechnology & Pharmaceutical'),
        ('Design & Manufacturing', 'Design & Manufacturing'),
        ('Innovation', 'Innovation'),
        ('Real Estate', 'Real Estate'),
        ('Leadership & Communication', 'Leadership & Communication'),
        ('Crisis Management', 'Biotechnology & Pharmaceutical'),
        ('Energy & Sustainability', 'Energy & Sustainability'),
)
    
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

class TrainingForm(forms.ModelForm):
    course = forms.CharField(label="Course", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$',
                                 message="Only letter is allowed!")], required=True,
                                 widget=forms.TextInput(attrs={'placeholder':'Course', 
                                                               'style':'font-size: 13px; text-transform: capitalize'}))
    
    lead_instructor = forms.CharField(label="Lead Instructor", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$',
                                 message="Only letter is allowed!")], required=True,
                                 widget=forms.TextInput(attrs={'placeholder':'Lead instructor', 
                                                               'style':'font-size: 13px; text-transform: capitalize'}))
    fees = forms.CharField(label="Fees", min_length=3, validators= [RegexValidator(r'^[a-zA-Z0-9-\s]*$',
                                 message="Only letter is allowed!")], required=True,
                                 widget=forms.TextInput(attrs={'placeholder':'Fees', 
                                                               'style':'font-size: 13px; text-transform: capitalize'}))
    location = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=LOCATION_CHOICES)
    topic = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=TOPIC_CHOICES)
    status = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=STATUS_CHOICES)
    course_description = forms.CharField(label="Course description", min_length=50, required=True,
                                 widget=forms.Textarea(attrs={'placeholder':'Write a brief course description', 
                                                               'style':'font-size: 13px', 'rows':4}))
    learning_outcome = forms.CharField(label="Learning Outcomes", min_length=50, required=True,
                                 widget=forms.Textarea(attrs={'placeholder':'Write a brief learning otcomes', 
                                                               'style':'font-size: 13px', 'rows':4}))
    curriculum = forms.CharField(label="Course Curriculum", min_length=50, required=True,
                                 widget=forms.Textarea(attrs={'placeholder':'Course Curriculum', 
                                                               'style':'font-size: 13px', 'rows':4}))
    date = forms.DateField(label="Date", required=False, widget=forms.DateInput(attrs={'class': 'form-control datepicker-input'}))

    
    class Meta:
        model = Training
        fields = ('course','lead_instructor', 'fees', 'location', 'location', 'topic', 'status', 
                  'course_description', 'learning_outcome', 'curriculum', 'date')
    
   

