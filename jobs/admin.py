from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_filter = ['title', 'company', 'location', 'sector']
    list_display = ['title', 'company', 'location', 'sector', 'contract', 'expiration_date']
    search_fields = ['title', 'company', 'location', 'sector']
    list_per_page = 10

admin.site.register(Job, JobAdmin)