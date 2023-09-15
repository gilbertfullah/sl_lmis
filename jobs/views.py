from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, AppliedJobs, SavedJobs, Location, Contract, JobApplication
from .form import JobForm, JobSearchForm, JobApplicationForm, JobApplicationWizard
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
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy




def Jobs(request):
    jobs = Job.objects.filter(job_status='Approved').order_by('-published_date')
    jobs_count = Job.objects.all().count()
    locations = Location.objects.all()
    sectors = Sector.objects.all()
    
    location_counts = {loc: Job.objects.filter(location=loc).count() for loc in locations}
    
    # Query to count jobs for each location
    locations_with_counts = Location.objects.annotate(job_count=Count('job'))
    
    location_filter = request.GET.get('location')
    
    if location_filter:
        jobs = Job.objects.filter(location=location_filter, job_status='Approved')
        
        paginator = Paginator(jobs, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    
    else:
        jobs = Job.objects.filter(job_status='Approved').order_by('-published_date')
        
        paginator = Paginator(jobs, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    # Calculate the number of job openings for each category
    categories = {}
    for job in jobs:
        category = job.sector
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1
    
    
    
    context = {
        'jobs': page_obj,
        'categories': categories,
        'jobs_count': jobs_count,
        'sectors': sectors,
        'locations': locations,
        'location_counts':location_counts,
        'locations_with_counts':locations_with_counts
    }
            
    return render(request, 'jobs.html', context)

def application_success(request):
    jobseeker = get_object_or_404(JobSeeker, user=request.user)
    return render(request, 'application_success.html', {'jobseeker':jobseeker})

@login_required
def save_job(request, job_id):
    user = request.user
    job = get_object_or_404(Job, id=job_id)
    employer = Employer.objects.get(company_name=job.employer)
    saved, created = SavedJobs.objects.get_or_create(job=job, jobseeker=user, employer=employer)
    return redirect('job_detail', job_id=job_id)

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    employer = Employer.objects.get(company_name=job.employer)
    related_jobs = Job.objects.filter(sector=job.sector).exclude(id=job_id)[:4]
    
    
    job_applied = False  # Initialize to False by default
    job_saved = False
    
    if request.user.is_authenticated:
        # Only perform the query if the user is authenticated
        job_applied = job.applications.filter(jobseeker=request.user).exists()
        job_saved = job.saved_job.filter(jobseeker=request.user).exists()
        # Create a form instance with initial data from the job seeker
        job_seeker = get_object_or_404(JobSeeker, user=request.user)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to the login page if not authenticated

        # Get the job seeker's information
        job_seeker = get_object_or_404(JobSeeker, user=request.user)

        form = JobApplicationForm(request.POST)
        if form.is_valid():
            # Create a JobApplication object
            job_application = form.save(commit=False)
            job_application.job = job
            job_application.jobseeker = job_seeker
            job_application.employer = job.employer
            job_application.save()

            # Send an email notification
            email_subject = f"New Job Application for: {job.title}"
            email_body = f"Job Seeker Full Name: {job_seeker.first_name} {job_seeker.last_name}\n"
            email_body += f"Email: {job_seeker.email}\n"
            email_body += f"Phone: {job_seeker.phone_number}\n"
            email_body += f"Job Seeker Resume: {job_seeker.resume}\n"
            email_body += f"Thank you for applying for the {job.title} job."

            #email = EmailMessage(email_subject, email_body, to=[job.employer.email, job_seeker.email])
            #email.send()

            # Create an AppliedJobs entry
            AppliedJobs.objects.get_or_create(job=job, user=job_seeker.user)

            return redirect('application_success')

    else:
            
            if request.user.is_authenticated:
                form = JobApplicationForm(initial={
                    'first_name': job_seeker.first_name,
                    'last_name': job_seeker.last_name,
                    'email': job_seeker.email,
                    'phone_number': job_seeker.phone_number,
                    'resume': job_seeker.resume,
                    # Add other fields based on your form
                })
            else:
                form = None
        
    context = {
        'related_jobs':related_jobs,
        'job': job,
        'job_applied': job_applied,
        'form': form,
        'employer': employer,
        'job_saved': job_saved,
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
def unsave_job(request, id):
    job = get_object_or_404(Job, id=id)
    SavedJob.objects.filter(jobseeker=request.user, job=job).delete()
    return redirect('job_detail', id=id) 


@login_required
def application_form(request):
    return render(request, "job_application.html")

@login_required
def apply_job(request, id):
    job = get_object_or_404(Job, id=id)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Assuming you have a User model for job seekers and they are authenticated
            jobseeker = get_object_or_404(JobSeeker, user=request.user)

            # Create a JobApplication object
            job_application = JobApplication(
                job=job,
                jobseeker=request.user,
                employer=job.employer,
            )
            job_application.save()
            
            # Send an email notification to the employer
            email_subject = f"New Job Application for: {job.title}"
            email_body = f"Job Seeker Full Name: {jobseeker.first_name} {jobseeker.last_name}\n"
            email_body += f"Email: {jobseeker.email}\n"
            email_body += f"Phone: {jobseeker.phone_number}\n"
            email_body += f"Job Seeker Resume: {jobseeker.resume}\n"
            email_body += f"Thank you for applying for the {job.title} job."
            
            email = EmailMessage(email_subject, email_body, to=[job.employer.email, jobseeker.email])
            email.send()
            
            # Create an AppliedJobs entry
            AppliedJobs.objects.get_or_create(job=job, user=jobseeker.user, employer=job.employer)

            # Redirect to a success page or wherever you need
            return redirect('application_success')
        
    else:
            # Create a new form instance without initial data
            # Create a form instance with initial data from the job seeker
            if request.user.is_authenticated:
                form = JobApplicationForm(initial={
                    'first_name': job_seeker.first_name,
                    'last_name': job_seeker.last_name,
                    'email': job_seeker.email,
                    'phone_number': job_seeker.phone_number,
                    'resume': job_seeker.resume,
                    # Add other fields based on your form
                })
            else:
                form = None
        
    return render(request, 'job_detail.html', {'form': form})

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



