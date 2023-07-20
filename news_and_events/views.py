from django.shortcuts import render
from .models import NewsAndEvents

def news_and_events(request):

    return render(request, 'news_and_events.html') 