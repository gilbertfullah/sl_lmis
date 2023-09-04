from .models import JobSeeker
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404



def jobseeker_id(request):
    if request.user.is_authenticated and request.user.is_jobseeker:
        jobseeker = get_object_or_404(JobSeeker, user=request.user)
        jobseeker_id = jobseeker.id
    else:
        jobseeker_id = None
    
    return {'id': jobseeker_id}