from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Count
from plotly.graph_objs import Pie
from jobs.models import Job
from django.db import models
from news_and_events.models import NewsAndEvents


def home(request):
    jobs = Job.objects.all().order_by('-published_date')[:6]
    news_and_events_list = NewsAndEvents.objects.all().order_by('-published_date')[:3]
    jobs_count = Job.objects.all().count()
    categories = Job.objects.values('sector').annotate(job_count=Count('sector')).order_by('-job_count')[:4]
            
    return render(request, 'core/home.html', {'jobs': jobs, 'categories': categories, 'news_and_events_list': news_and_events_list, 'jobs_count': jobs_count})

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
