from django.shortcuts import render
from django.conf import settings
from django.http.response import HttpResponse
import mimetypes
from .models import IndustrialRelation

def lmi(request):
    return render(request, 'labour_supply.html')

def employment(request):
    return render(request, 'employment.html')

def unemployment(request):
    return render(request, 'unemployment.html')

def employer_insight(request):
    return render(request, 'employer_insight.html')

def recruitment_insight(request):
    return render(request, 'recruitment_insight.html')

def industrial_relations(request):
    cases = IndustrialRelation.objects.all()
    num_cases = cases.count()
    num_pending = cases.filter(status='Pending').count()
    num_settled = cases.filter(status='Settled').count()
    num_court = cases.filter(status='Court').count()
    context = {
        'num_cases': num_cases,
        'num_pending': num_pending,
        'num_settled': num_settled,
        'num_court': num_court,
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
