from django.shortcuts import render, get_object_or_404
from .models import NewsAndEvents

def news_and_events(request):
    news_and_events_list = NewsAndEvents.objects.all()
    
    paginator = Paginator(news_and_events_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'news_and_events_list': page_obj}
    
    return render(request, 'news_and_events.html', context) 

def news_and_event_detail(request, news_id):
    news = get_object_or_404(NewsAndEvents, pk=news_id)
    context = {'news': news}
    return render(request, 'news_and_event_details.html', context)