from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic.edit import CreateView
from .form import JobSeekerRegisterForm, CompanyRegisterForm, GovernmentRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, JobSeeker, Employer, Government, ProfileView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
#from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
import os
from django.conf import settings
import calendar
from django.db.models.functions import ExtractMonth, ExtractHour, ExtractDay
from django.db.models import Count
from jobs.models import SavedJobs, AppliedJobs, Job
from datetime import timedelta
from django.utils import timezone
#import json

def register(request):
    return render(request, 'register.html')

def JobSeekerRegister(request):
    if request.user.is_authenticated:
        return redirect("login")
    else:
        if request.method == "POST":
            form = JobSeekerRegisterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f"{user} was successfully registered")
                return redirect("login")
        else:
            form = JobSeekerRegisterForm()
            messages.error(request, "Form is not valid")
            context = {'form':form}
            return render(request, 'jobseeker_register.html', context)

    return render(request, 'jobseeker_register.html', {'form':form})

def employer(request):
    # Fetch all employers
    employers = Employer.objects.all()

    employer_data = []
    for employer in employers:
        # For each employer, get their job listings and count them
        job_listings_for_employer = Job.objects.filter(employer=employer)
        job_count = job_listings_for_employer.count()

        # Create a dictionary with employer details and job count
        employer_info = {
            'employer': employer,
            'job_count': job_count,
        }

        # Append this dictionary to the employer_data list
        employer_data.append(employer_info)

    paginator = Paginator(employer_data, 6)  # Paginate the employer data
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'employers': page_obj,
    }

    if not employers:
        return render(request, 'blank_employer_page.html')  # Create a 'blank_employer_page.html' template for this purpose

    return render(request, 'employers.html', context)



def employer_job_listings(request, employer_id):
    employer = get_object_or_404(Employer, id=employer_id)
    # Get all job listings for the specific employer
    job_listings = Job.objects.filter(employer=employer)

    context = {
        'employer': employer,
        'job_listings': job_listings,
    }
    
    return render(request, 'employer_job_listings.html', context)

def employer_details(request, employer_id):
    employer = get_object_or_404(Employer, id=employer_id)
    job_openings = Job.objects.filter(employer=employer)

    context = {
        'employer': employer,
        'job_openings': job_openings,
    }

    return render(request, 'employer_details.html', context)

@login_required
def jobseeker_profile(request, id):
    #jobseeker = JobSeeker.objects.get(user=request.user)
    #employer = Employer.objects.get(user=request.user)
    jobseeker = get_object_or_404(JobSeeker, id=id)
    
    if request.user.is_authenticated:
    
        context = {
            'jobseeker': jobseeker,
            #'employer': employer,
        }
    
        return render(request, 'jobseeker_profile.html', context)
    else:
        return render(request, 'signin.html')

@login_required
def edit_jobseeker_profile(request, id):
    jobseeker_profile = JobSeeker.objects.get(id=id)
    #profile = JobSeeker.objects.filter(user=you).first()
    if request.method == 'POST':
        form = JobseekerProfileForm(request.POST, request.FILES, instance=jobseeker_profile)
        if form.is_valid():
            form.save()
            return redirect('jobseeker_profile')
    else:
        form = JobseekerProfileForm(instance=jobseeker_profile)
    context = {
        'form': form,
    }
    return render(request, 'edit_jobseeker_profile.html', context)

@login_required
def jobseeker_profile_view(request, id):
    jobseeker = get_object_or_404(JobSeeker, id=id)
    
    # Record the profile view
    if request.user.is_authenticated:
        # Ensure the user is authenticated before recording the view
        profile_view, created = ProfileView.objects.get_or_create(
            viewer=request.user,
            jobseeker=jobseeker,
        )
    
    if request.user.is_authenticated:
        # Prevent multiple views within a time period (e.g., 1 hour)
        one_hour_ago = timezone.now() - timedelta(hours=1)
        existing_views = ProfileView.objects.filter(
            viewer=request.user,
            jobseeker=jobseeker,
            timestamp__gte=one_hour_ago,
        )
        if not existing_views.exists():
            profile_view = ProfileView(
                viewer=request.user,
                jobseeker=jobseeker,
            )
            profile_view.save()
            
    context = {
        'jobseeker': jobseeker,
    }
        
    return render(request, 'jobseeker_profile.html', context)

def viewed_by_users(request, jobseeker_id):
    # Query ProfileView to get users who viewed the jobseeker's profile
    profile_views = ProfileView.objects.filter(jobseeker_id=jobseeker_id).select_related('viewer__username')

    # Extract the usernames of users who viewed the profile
    viewed_by_usernames = [view.viewer.username for view in profile_views]

    context = {
        'jobseeker_id': jobseeker_id,
        'viewed_by_usernames': viewed_by_usernames,
    }

    return render(request, 'viewed_by_users.html', context)


def jobseeker_details(request):
    return render(request, 'details.html')

@login_required
@csrf_exempt
def delete_skill(request, pk=None):
    if request.method == 'POST':
        id_list = request.POST.getlist('choices')
        for skill_id in id_list:
            Skill.objects.get(id=skill_id).delete()
        return redirect('profile')


def CompanyRegister(request):
    if request.user.is_authenticated:
        return redirect("login")
    else:
        if request.method == "POST":
            form = CompanyRegisterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                company_name = form.cleaned_data.get('company_name')
                messages.success(request, f"{company_name} was successfully registered")
                return redirect("login")
        else:
            form = CompanyRegisterForm()
            messages.error(request, "Form is not valid")
            context = {'form':form}
            return render(request, 'company_register.html', context)

    return render(request, 'company_register.html', {'form':form})

    
def GovernmentRegister(request):
    if request.user.is_authenticated:
        return redirect("login")
    else:
        if request.method == "POST":
            form = GovernmentRegisterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('government_institution_name')
                messages.success(request, f"{user} was successfully registered")
                return redirect("login")
        else:
            form = GovernmentRegisterForm()
            messages.error(request, "Form is not valid")
            context = {'form':form}
            return render(request, 'government_register.html', context)

    return render(request, 'government_register.html', {'form':form})
    

def login_request(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return '/jobseeker_dashboard/'
                else:
                    messages.error(request,"Invalid username or password")
            else:
                messages.error(request,"Invalid username or password")
    form = AuthenticationForm()
    return render(request, 'signin.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('/')

def rec_details(request):
    context = {
        'rec_home_page': "active",
        'rec_navbar': 1,
    }
    return render(request, 'details.html', context)

@login_required
def dashboard(request):
    current_user = request.user
    
    if current_user.is_jobseeker:
         
        template = 'jobseeker_dashboard.html'
    elif current_user.is_company:
        template = 'employer_dashboard.html'
    elif current_user.is_government:
        template = 'gov_dashboard.html'
    else:
        template = 'admin_dashboard.html'
        
    return render(request, template)

@login_required
def jobseeker_dashboard(request):
    jobseeker = request.user.is_jobseeker
    if request.user.is_authenticated:
        if jobseeker:
            saved_jobs = SavedJobs.objects.filter(jobseeker=request.user)
            total_saved_jobs = saved_jobs.count()
            saved_jobs_by_month = saved_jobs.annotate(month=ExtractMonth('saved_at')).values('month')\
            .annotate(count=Count('id', distinct=True)).values('month', 'count')
            
            months = []
            total_saved_jobs_by_month = []
            
            for job in saved_jobs_by_month:
                months.append(calendar.month_name[job["month"]])
                total_saved_jobs_by_month.append(job["count"])
                
            
            profile_views = ProfileView.objects.filter(jobseeker=jobseeker)
            
            total_views = ProfileView.objects.filter(jobseeker=jobseeker).count()
            
            views_by_day = profile_views.annotate(day=ExtractDay('timestamp')).values('day').annotate(count=Count('id', distinct=True)).order_by('day')
            
            days = []
            viewCounts = []
            
            for view in views_by_day:
                day_number = view['day']
                day_name = calendar.day_name[day_name - 1]
                view_count = view['count']
                
                days.append(day_name)
                viewCounts.append(view_count)
            #profile_view_by_hour = profile_view.annotate(hour=ExtractHour('timestamp')).values('hour')\
            #.annotate(count=Count('id', distinct=True)).values('hour', 'count')
            
            #hours = []
            #hourly_views = []
            
            #for p in profile_view_by_hour:
                #months.append(p["hour"])
                #hourly_views.append(p["count"])

            job_applications = AppliedJobs.objects.filter(user=request.user)
            
            total_job_applications = AppliedJobs.objects.filter(user=request.user).count()
            
            applied_jobs_by_day = job_applications.annotate(day=ExtractDay('date_applied')).values('day').annotate(count=Count('id', distinct=True)).order_by('day')
            
            applied_by_day = []
            count_by_day = []
            
            for view in applied_jobs_by_day:
                for job in saved_jobs_by_month:
                    applied_by_day.append(calendar.day_name[view["day"]])
                    count_by_day.append(view["count"])
                
                applied_by_day = view['day']
                day_name = calendar.day_name[applied_by_day - 1]
                count_by_day = view['count']
                
                applied_by_day.append(day_name)
                count_by_day.append(count_by_day)
                
            profile_views = ProfileView.objects.filter(jobseeker=jobseeker)

            # Extract the usernames of users who viewed the profile
            viewed_by_usernames = [view.viewer.username for view in profile_views]
            
            
            context = {
                'saved_jobs': saved_jobs,
                'total_saved_jobs': total_saved_jobs,
                'saved_jobs_by_month': saved_jobs_by_month,
                'months': months,
                'total_saved_jobs_by_month': total_saved_jobs_by_month,
                'total_views': total_views,
                'days': days,
                'viewCounts': viewCounts,
                'job_applications': job_applications,
                'total_job_applications': total_job_applications,
                'applied_by_day': applied_by_day,
                'count_by_day': count_by_day,
                'jobseeker': jobseeker,
                'viewed_by_usernames': viewed_by_usernames,
            }
        
            return render(request, 'jobseeker_dashboard.html', context)
        else:
            return redirect('employer_dashboard')
    else:
        # User is not authenticated, redirect to the login page or show a message
        return redirect('login')