from django.shortcuts import render
from .models import Institution

def career_dev(request):
    institutions = Institution.objects.all()
    context = {'institutions': institutions}
    
    return render(request, "career_dev.html", context)