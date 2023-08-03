from django.contrib import admin
from .models import DownloadDocument

class DownloadDocsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 10

    
admin.site.register(DownloadDocument, DownloadDocsAdmin)