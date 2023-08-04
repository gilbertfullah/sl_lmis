from django.shortcuts import render
from .models import NewsAndEvents

def news_and_events(request):
    news_and_events_list = NewsAndEvents.objects.all()
    context = {'news_and_events_list': news_and_events_list}
    
    
    return render(request, 'news_and_events.html') 

def news_and_event_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    context = {'news': news}
    return render(request, 'news_and_event_details.html', context)