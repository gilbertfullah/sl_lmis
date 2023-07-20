from django.shortcuts import render
from .models import NewsAndEvents, Image

def news_and_events(request):
    news_and_events = NewsAndEvents.objects.all()
    context = {'news_and_events': news_and_events}
    return render(request, 'news_and_events.html', context) 