from django.shortcuts import render
from django.conf import settings
from django.http.response import HttpResponse
import mimetypes
from .models import IndustrialRelation, SalaryInformation
import plotly.graph_objs as go
import plotly.offline as pyo

def lmi(request):
    return render(request, 'lmi.html')

def employment_statistics(request):
    return render(request, 'employment_statistics.html')

def industrial_relations(request):
    cases = IndustrialRelation.objects.all()
    num_cases = cases.count()
    num_pending = cases.filter(complaint_status='Pending').count()
    num_settled = cases.filter(complaint_status='Settled').count()
    num_court = cases.filter(complaint_status='Court').count()
    
    # create data for plot
    x = ['Settled', 'Pending', 'Court']
    y = [45, 15, 5]

    # create plotly figure
    fig = go.Figure(
        data=[go.Bar(x=x, y=y)],
        layout=go.Layout(title='Industrial Cases')
    )

    # convert plotly figure to HTML
    plot_div = pyo.plot(fig, output_type='div')
    
    context = {
        'num_cases': num_cases,
        'num_pending': num_pending,
        'num_settled': num_settled,
        'num_court': num_court,
        'plot_div': plot_div,
    }

    return render(request, 'industrial_relations.html', context)

def download_file(request):
    # Define Django project base directory
    BASE_DIR = settings.MEDIA_ROOT
    # Define text file name
    filename = 'CV.pdf'
    # Define the full file path
    filepath = BASE_DIR + '/images/' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

def salary_information(request):
    job_title = request.GET.get('job_title')
    location = request.GET.get('location')
    industry = request.GET.get('industry')
    date = request.GET.get('date')

    salary_info = SalaryInformation.objects.filter(job_title=job_title, location=location, industry=industry, date=date)
    context = {'salary_info': salary_info}
    return render(request, 'salary_information.html', context)

def industry_trends(request):
    industry = request.GET.get('industry')
    location = request.GET.get('location')
    date = request.GET.get('date')

    trends = IndustryTrends.objects.filter(industry=industry, location=location, date=date)
    context = {'trends': trends}
    return render(request, 'industry_trends.html', context)

def employment_insights(request):
    industry = request.GET.get('industry')
    location = request.GET.get('location')
    date = request.GET.get('date')

    insights = EmploymentInsights.objects.filter(industry=industry, location=location, date=date)
    context = {'insights': insights}
    return render(request, 'employment_insights.html', context)


