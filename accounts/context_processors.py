from .models import JobSeeker, Employer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404



def jobseeker_id(request):
    if request.user.is_authenticated and request.user.is_jobseeker:
        jobseeker = get_object_or_404(JobSeeker, user=request.user)
        jobseeker_id = jobseeker.id
    else:
        jobseeker_id = None
    
    return {'jobseeker_id': jobseeker_id}

def employer_id(request):
    if request.user.is_authenticated and request.user.is_company:
        employer = get_object_or_404(Employer, user=request.user)
        employer_id = employer.id
    else:
        employer_id = None
    
    return {'id': employer_id}