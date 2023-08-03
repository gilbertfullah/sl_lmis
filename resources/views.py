from django.shortcuts import render
from .models import DownloadDocument

def resources(request):
    return render(request, 'resources.html')

def download_list(request):
    downloads = DownloadDocument.objects.all()
    context = {
        'downloads': downloads,
    }
    return render(request, 'downloads.html', context)

def download_document(request, document_id):
    document = get_object_or_404(DownloadDocument, pk=document_id)
    file_path = document.file.path
    response = FileResponse(open(file_path, 'rb'))
    return response