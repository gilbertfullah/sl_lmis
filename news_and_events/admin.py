from django.contrib import admin
from .models import NewsAndEvents, Image

class NewsAndEventsAdmin(admin.ModelAdmin):
    list_filter = ['title', 'tag', 'author']
    list_display = ['title', 'tag', 'author', 'published_date']
    search_fields = ['title', 'tag', 'author']
    list_per_page = 10

    
admin.site.register(NewsAndEvents, NewsAndEventsAdmin)
admin.site.register(Image)