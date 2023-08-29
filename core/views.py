from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Count
from plotly.graph_objs import Pie
from jobs.models import Job, Sector
from django.db import models
from news_and_events.models import NewsAndEvents
from .models import LFP, EmploymentAndUnemployment
from taggit.models import Tag


def home(request):
    jobs = Job.objects.filter(job_status='Approved').order_by('-published_date')[:6]
    news_and_events_list = NewsAndEvents.objects.all().order_by('-published_date')[:3]
    jobs_count = Job.objects.all().count()
    
    #sectors = Sector.objects.all()
    #sector_count = Sector.objects.values('sector').annotate(job_count=Count('sector'))
    sectors = Sector.objects.annotate(job_count=Count('job'))[:8]
    
    context = {
        'jobs': jobs,
        'sectors': sectors,
        'news_and_events_list': news_and_events_list,
        'jobs_count': jobs_count
    }
    
    return render(request, 'core/home.html', context)

def lfp(request):
    lfp = LFP.objects.all()
    return render(request, "core/lfp.html", {'lfp':lfp})

def employment_and_unemployment(request):
    employment_and_unemployment = EmploymentAndUnemployment.objects.all()
    return render(request, "core/eau.html", {'employment_and_unemployment': employment_and_unemployment})

def news_and_event_detail(request, news_id):
    news = get_object_or_404(NewsAndEvents, pk=news_id)
    context = {'news': news}
    return render(request, 'news_and_event_details.html', context)

def working_age_population(request):
    values = [20, 30, 40, 50]
    labels = ['A', 'B', 'C', 'D']

    data = [Pie(values=values, labels=labels)]

    return render(request, 'my_template.html', {'data': data})

def employment_rate(request):
    values = [5.2]
    labels = ['Employment Rate']

    employment_data = [Pie(values=values, labels=labels, hoverinfo='label+percent', textinfo='value', textposition='inside', hole=.4,
        domain={'x': [0, 1], 'y': [0, 1]}, title='Unemployment Rate', titleposition='top center', type='pie', showlegend=False,
        annotations=[dict(showarrow=False, text='5.2%', x=0.5, y=0.5, font=dict(size=20, color='white'), align='center', bgcolor='black',
        opacity=0.5)])]

    return render(request, 'home.html', {'employment_data': employment_data})

def unemployment_rate(request):
    values = [5.33]
    labels = ['Employment Rate']

    unemployment_data = [Pie(values=values, labels=labels, hoverinfo='label+percent', textinfo='value', textposition='inside', hole=.4,
        domain={'x': [0, 1], 'y': [0, 1]}, title='Unemployment Rate', titleposition='top center', type='pie', showlegend=False,
        annotations=[dict(showarrow=False, text='5.33%', x=0.5, y=0.5, font=dict(size=20, color='white'), align='center', bgcolor='black',
        opacity=0.5)])]

    return render(request, 'home.html', {'unemployment_data': unemployment_data})

def youth_unemployment_rate(request):
    values = [10.44]
    labels = ['Employment Rate']

    data = [Pie(values=values, labels=labels, hoverinfo='label+percent', textinfo='value', textposition='inside', hole=.4,
        domain={'x': [0, 1], 'y': [0, 1]}, title='Unemployment Rate', titleposition='top center', type='pie', showlegend=False,
        annotations=[dict(showarrow=False, text='10.44%', x=0.5, y=0.5, font=dict(size=20, color='white'), align='center', bgcolor='black',
        opacity=0.5)])]

    return render(request, 'home.html', {'data': data})


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
    
    return render(request, 'jobs/job_detail.html', context)

def tag_list(request, tag_slug=None):
    jobs = Job.objects.filter(job_status='Approved').order_by('-published_date')
    
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        jobs = Job.objects.filter(tags__in=[tag])
    
    context = {
        "jobs": jobs,
        "tag": tag,
        }
    
    return render(request, 'jobs/tag.html', context)