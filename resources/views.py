from django.shortcuts import render
from .models import DownloadDocument

def download_list(request):
    downloads = DownloadDocument.objects.all()
    context = {
        'downloads': downloads,
    }
    return render(request, 'downloads.html', context)