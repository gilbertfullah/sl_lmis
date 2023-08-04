from django.shortcuts import render
from .models import DownloadDocument
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