from django.shortcuts import render
from django.db.models import Q
from django.db.models import Count
from .form import TrainingForm
from django.contrib import messages
from .models import Training
from django.core.paginator import Paginator, EmptyPage

def training_programs(request):
    query = request.GET.get('p')
    
    if query:
        trainings = Training.objects.filter(Q(course__icontains=query))
    else:
        trainings = Training.objects.all()
        
    paginator = Paginator(trainings, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'trainings': page_obj, 'query': query, 'trainings_count':Training.objects.all().count()}
    
    return render(request, "training.html", context)
