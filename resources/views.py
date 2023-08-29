from django.shortcuts import render
from .models import DownloadDocument, LabourLaw, PolicyAndRegulation, ReportAndSurvey
from django.core.paginator import Paginator, EmptyPage

def download_list(request):
    downloads = DownloadDocument.objects.all()
    
    paginator = Paginator(downloads, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'downloads': page_obj,
    }
    return render(request, 'downloads.html', context)

def labourlaws(request):
    downloads = LabourLaw.objects.all()
    
    paginator = Paginator(downloads, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'labourlaws': page_obj,
    }
    return render(request, 'labour_laws.html', context)

def policy_and_regulation(request):
    downloads = PolicyAndRegulation.objects.all()
    
    paginator = Paginator(downloads, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'policies': page_obj,
    }
    return render(request, 'policies_and_regulations.html', context)

def report_and_survey(request):
    downloads = ReportAndSurvey.objects.all()
    
    paginator = Paginator(downloads, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'reports': page_obj,
    }
    return render(request, 'reports_and_surveys.html', context)