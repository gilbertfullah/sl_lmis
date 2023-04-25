from django.contrib import admin
from .models import Training

class TrainingAdmin(admin.ModelAdmin):
    list_filter = ['course', 'topic', 'location', 'status']
    list_display = ['course', 'topic', 'date', 'location', 'lead_instructor', 'fees', 'status']
    search_fields = ['course', 'topic']
    list_per_page = 10

admin.site.register(Training, TrainingAdmin)