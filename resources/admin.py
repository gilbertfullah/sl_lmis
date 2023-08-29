from django.contrib import admin
from .models import DownloadDocument, LabourLaw, PolicyAndRegulation, ReportAndSurvey

class DownloadDocsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 10

class LabourLawAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 10

class PolicyAndRegulationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 10
    
class ReportAndSurveyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 10
    
    
admin.site.register(DownloadDocument, DownloadDocsAdmin)
admin.site.register(LabourLaw, LabourLawAdmin)
admin.site.register(PolicyAndRegulation, PolicyAndRegulationAdmin)
admin.site.register(ReportAndSurvey, ReportAndSurveyAdmin)