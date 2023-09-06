from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, AppliedJobs, SavedJobs, Location, Contract, JobApplication
from .form import JobForm, JobSearchForm, JobApplicationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .decorators import allowed_users
from django.contrib import messages
from accounts.models import Employer, Government, User, JobSeeker
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
from django.conf import settings
from django.db.models import Q
from django.db.models import Count
from django.views.generic import TemplateView
from .models import Job, Sector
from taggit.models import Tag
from django.core.mail import EmailMessage



def Jobs(request):
    jobs = Job.objects.filter(job_status='Approved').order_by('-published_date')
    jobs_count = Job.objects.all().count()
    locations = Location.objects.all()
    sectors = Sector.objects.all()
    
    location_counts = {loc: Job.objects.filter(location=loc).count() for loc in locations}
    
    # Query to count jobs for each location
    locations_with_counts = Location.objects.annotate(job_count=Count('job'))

    # Calculate the number of job openings for each category
    categories = {}
    for job in jobs:
        category = job.sector
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1
    
    paginator = Paginator(jobs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
            
    return render(request, 'jobs.html', {'jobs': page_obj, 'categories': categories, 'jobs_count': jobs_count, 'sectors': sectors, 'locations': locations, 'location_counts':location_counts, 'locations_with_counts':locations_with_counts})

def job_detail(request, id):
    job_detail = get_object_or_404(Job, id=id)
    employer = Employer.objects.get(company_name=job_detail.employer)
    related_jobs = Job.objects.filter(sector=job_detail.sector).exclude(id=id)[:4]

    
    context = {
        'related_jobs':related_jobs, 
        'job_detail': job_detail,
        'employer': employer,
        }
    
    return render(request, 'job_detail.html', context)

def sectors(request):
    #sectors = Sector.objects.all()
    sectors = Sector.objects.annotate(job_count=Count('job'))
    
    #related_job_sectors = Job.objects.filter(sector=sectors.title)
    
    context = {
        'sectors': sectors,
        #"related_job_sectors": related_job_sectors,
        }
    return render(request, 'sectors.html', context)

def sector_detail(request, id):
    sector = Sector.objects.get(id=id)
    related_job_sectors = Job.objects.filter(sector=sector.id)
    count = Job.objects.filter(sector=sector.id).count()
    
    paginator = Paginator(related_job_sectors, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        "sector": sector,
        "related_job_sectors": page_obj,
        'count': count,
        }
    
    return render(request, 'sector_detail.html', context)

def favourite(request, id):
    job = get_object_or_404(Job, id=id)
    if job.favourite.filter(id=request.user.id).exists():
        job.favourite.remove(request.user)
    else:
        job.favourite.add(request.user)
    return render(request, 'jobs_favourite_list.html')

def jobs_favourite_list(request):
    user = request.user
    favourite_jobs = user.favourite.all()
    
    context = {
        'favourite_jobs': favourite_jobs
    }

    return render(request, 'jobs_favourite_list.html', context)

@login_required
def post_job(request):
    user = request.user.employer  
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.employer = user
            data.save()
            messages.success(request, f"Job was successfully registered")
            return redirect("jobs")
    else:
        messages.error(request, "Form is not valid")
        form = JobForm()
        
    context = {
        'form': form,
    }
    return render(request, 'post_job.html', context)

@login_required
def save_job(request, id):
    user = request.user
    job = get_object_or_404(Job, id=id)
    employer = Employer.objects.get(company_name=job.employer)
    saved, created = SavedJobs.objects.get_or_create(job=job, jobseeker=user, employer=employer)
    return redirect('job_detail', id=id)

@login_required
def unsave_job(request, id):
    job = get_object_or_404(Job, id=id)
    SavedJob.objects.filter(jobseeker=request.user, job=job).delete()
    return redirect('job_detail', id=id) 



@login_required
def apply_job(request, id):
    if request.method == 'POST':
        jobseeker = request.user
        
        job = Job.objects.get(id=id)
        job_application = JobApplication.objects.create(job=job, jobseeker=jobseeker, employer=job.employer)
        job_application.save()
        
        seeker = get_object_or_404(JobSeeker, user=request.user)
        
        first_name = jobseeker.first_name,
        last_name = jobseeker.last_name,
        email = jobseeker.email,
        phone_number = seeker.phone_number,
        resume = seeker.resume,
        title = job.title
        
        # Send an email notification
        email_subject = f"New Job Application for: {title}"
        email_body = f"Job Seeker FUll Name: {first_name} {last_name}\n"
        email_body += f"Email: {email}\n"
        email_body += f"Phone: {phone_number}\n"
        email_body += f"Job Seeker Resume: {resume}\n"
        email_body += f"Thank you for applying for the {title} job."
        
        email = EmailMessage(email_subject, email_body, to=[job.employer.email, email])
        email.send()

        
        applied, created = AppliedJobs.objects.get_or_create(job=job, user=jobseeker)
        
        context = {
        'jobseeker': seeker,
        'job': job
        }
        
        return render(request, 'application_success.html', context)
    
    # Handle GET requests and render the job application form
    job = Job.objects.get(id=id)
    #employer = request.user.is_company
    jobseeker = request.user.is_jobseeker
    
    context = {
        'job': job,
        }
    
    return render(request, 'job_detail.html', context)

@login_required
def remove_job(request, id):
    user = request.user
    job = get_object_or_404(Job, id=id)
    saved_job = SavedJobs.objects.filter(job=job, user=user).first()
    saved_job.delete()
    return HttpResponseRedirect('jobs')

@login_required
def remove_saved_job(request, saved_job_id):
    saved_job = get_object_or_404(SavedJobs, id=saved_job_id)
    
    if saved_job.jobseeker == request.user:  # Assuming jobseeker is the owner
        saved_job.delete()

    return redirect('jobseeker_dashboard')

@login_required
def saved_jobs(request):
    jobs = SavedJobs.objects.filter(user=request.user).order_by('-date_posted')
    return render(request, 'saved_jobs.html', {'jobs': jobs, 'candidate_navbar': 1})

@login_required
def applied_jobs(request):
    job_applications = AppliedJobs.objects.filter(user=request.user)

    return render(request, 'applied_jobs.html', {'job_applications': job_applications,})


def tag_list(request, tag_slug=None):
    jobs = Job.objects.filter(job_status='Approved').order_by('-published_date')
    
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        jobs = Job.objects.filter(tags__in=[tag])
    
    paginator = Paginator(jobs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        "jobs": page_obj,
        "tag": tag,
        }
    
    return render(request, 'tag.html', context)

def job_search(request):
    query = request.GET.get('jobTitle')
    location = request.GET.get('location')
    sector = request.GET.get('sector')
    
    jobs = Job.objects.all()

    if query:
        jobs = jobs.filter(title__icontains=query).order_by("-published_date")

    if location:
        jobs = jobs.filter(location__icontains=location).order_by("-published_date")

    if sector:
        jobs = jobs.filter(sector=sector).order_by("-published_date")

    #jobs = Job.objects.filter(title__icontains=query).order_by("-published_date")
    
    
    context = {'jobs': jobs, 'query': query, 'location': location, 'sector': sector,}

    #context = {'jobs': jobs, 'query': query}
    return render(request, 'job_search_list.html', context)
