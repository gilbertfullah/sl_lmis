from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, AppliedJobs, SavedJobs
from .form import JobForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .decorators import allowed_users
from django.contrib import messages
from accounts.models import Company, Government, User, JobSeeker, Skill
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
from django.conf import settings
from django.db.models import Q
from django.db.models import Count
from django.views.generic import TemplateView
from .models import Job


def Jobs(request):
    jobs = Job.objects.all()
    jobs_count = Job.objects.all().count()
    
    # Calculate the number of job openings for each category
    categories = {}
    for job in jobs:
        category = job.sector
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1
    
    paginator = Paginator(jobs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
            
    return render(request, 'jobs.html', {'jobs': page_obj, 'categories': categories, 'jobs_count': jobs_count})


def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    apply_button = 0
    save_button = 0
    profile = JobSeeker.objects.filter(user=request.user).first()
    if AppliedJobs.objects.filter(user=request.user).filter(job=job).exists():
        apply_button = 1
    if SavedJobs.objects.filter(user=request.user).filter(job=job).exists():
        save_button = 1
    relevant_jobs = []
    jobs1 = Job.objects.filter(company=job.company).order_by('-created_at')
    jobs2 = Job.objects.filter(contract=job.contract).order_by('-created_at')
    jobs3 = Job.objects.filter(title=job.title).order_by('-created_at')
    
    for i in jobs1:
        if len(relevant_jobs) > 5:
            break
        if i not in relevant_jobs and i != job:
            relevant_jobs.append(i)
    for i in jobs2:
        if len(relevant_jobs) > 5:
            break
        if i not in relevant_jobs and i != job:
            relevant_jobs.append(i)
    for i in jobs3:
        if len(relevant_jobs) > 5:
            break
        if i not in relevant_jobs and i != job:
            relevant_jobs.append(i)

    title = job.title
    sector = job.sector
    contract = job.contract
    description = job.description
    location = job.location
    expiration_date = job.expiration_date
    experience = job.experience
    qualification = job.qualification
    company = job.company
    requirements = job.requirements
    salary = job.salary
    
    context = {'description':description, 'location':location, 'expiration_date':expiration_date,
               'experience':experience, 'qualification':qualification, 'company':company, 'requirements':requirements,
               'contract': contract, 'title':title, 'sector':sector, 'salary':salary, 'job': job, 'profile': profile, 
               'apply_button': apply_button, 'save_button': save_button, 'relevant_jobs': relevant_jobs, 'candidate_navbar': 1}
    
    return render(request, 'job_detail.html', context)

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
    user = request.user
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.company = user
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


def job_search_list(request):
    query = request.GET.get('p')
    loc = request.GET.get('q')
    object_list = []
    if(query == None):
        object_list = Job.objects.all()
    else:
        title_list = Job.objects.filter(title__icontains=query).order_by('-date_posted')
        skill_list = Job.objects.filter(skills_req__icontains=query).order_by('-date_posted')
        company_list = Job.objects.filter(company__icontains=query).order_by('-date_posted')
        job_type_list = Job.objects.filter(job_type__icontains=query).order_by('-date_posted')
        for i in title_list:
            object_list.append(i)
        for i in skill_list:
            if i not in object_list:
                object_list.append(i)
        for i in company_list:
            if i not in object_list:
                object_list.append(i)
        for i in job_type_list:
            if i not in object_list:
                object_list.append(i)
    if(loc == None):
        locat = Job.objects.all()
    else:
        locat = Job.objects.filter(location__icontains=loc).order_by('-date_posted')
    final_list = []
    for i in object_list:
        if i in locat:
            final_list.append(i)
    paginator = Paginator(final_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'jobs': page_obj,
        'query': query,
    }
    return render(request, 'job_search_list.html', context)

@login_required
def save_job(request, id):
    user = request.user
    job = get_object_or_404(Job, id=id)
    saved, created = SavedJobs.objects.get_or_create(job=job, user=user)
    return HttpResponseRedirect('jobs')

@login_required
def apply_job(request, id):
    user = request.user
    job = get_object_or_404(Job, id=id)
    applied, created = AppliedJobs.objects.get_or_create(job=job, user=user)
    applicant, creation = Applicants.objects.get_or_create(job=job, applicant=user)
    return HttpResponseRedirect('jobs')

@login_required
def remove_job(request, id):
    user = request.user
    job = get_object_or_404(Job, id=id)
    saved_job = SavedJobs.objects.filter(job=job, user=user).first()
    saved_job.delete()
    return HttpResponseRedirect('jobs')

@login_required
def saved_jobs(request):
    jobs = SavedJobs.objects.filter(user=request.user).order_by('-date_posted')
    return render(request, 'saved_jobs.html', {'jobs': jobs, 'candidate_navbar': 1})

@login_required
def applied_jobs(request):
    jobs = AppliedJobs.objects.filter(user=request.user).order_by('-date_posted')
    statuses = []
    for job in jobs:
        if Selected.objects.filter(job=job.job).filter(applicant=request.user).exists():
            statuses.append(0)
        elif Applicants.objects.filter(job=job.job).filter(applicant=request.user).exists():
            statuses.append(1)
        else:
            statuses.append(2)
    zipped = zip(jobs, statuses)
    return render(request, 'applied_jobs.html', {'zipped': zipped, 'candidate_navbar': 1})

@login_required
def intelligent_search(request):
    relevant_jobs = []
    common = []
    job_skills = []
    user = request.user
    profile = JobSeeker.objects.filter(user=user).first()
    my_skill_query = Skill.objects.filter(user=user)
    my_skills = []
    for i in my_skill_query:
        my_skills.append(i.skill.lower())
    if profile:
        jobs = Job.objects.filter(job_type=profile.looking_for).order_by('-date_posted')
    else:
        jobs = Job.objects.all()
    for job in jobs:
        skills = []
        sk = str(job.skills_req).split(",")
        for i in sk:
            skills.append(i.strip().lower())
        common_skills = list(set(my_skills) & set(skills))
        if (len(common_skills) != 0 and len(common_skills) >= len(skills)//2):
            relevant_jobs.append(job)
            common.append(len(common_skills))
            job_skills.append(len(skills))
    objects = zip(relevant_jobs, common, job_skills)
    objects = sorted(objects, key=lambda t: t[1]/t[2], reverse=True)
    objects = objects[:100]
    context = {
        'intel_page': "active",
        'jobs': objects,
        'counter': len(relevant_jobs),
    }
    return render(request, 'intelligent_search.html', context)

