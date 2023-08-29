from django.contrib import admin
from django.utils.html import mark_safe
from .models import Job, Sector, SavedJobs, AppliedJobs

class JobAdmin(admin.ModelAdmin):
    list_filter = ['title', 'employer', 'location', 'sector']
    list_display = ['title', 'employer', 'image_preview', 'location', 'sector', 'contract', 'expiration_date']
    search_fields = ['title', 'employer', 'location', 'sector']
    list_per_page = 10
    
    def image_preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" alt="{obj.title}" width="60" height="60" />')
    image_preview.short_description = 'Image Preview'

class SectorAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_preview']
    
    def image_preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" alt="{obj.title}" width="60" height="60" />')
    image_preview.short_description = 'Image Preview'



class SavedAdmin(admin.ModelAdmin):
    list_display = ['user', 'job']
    list_per_page = 10
    
class AppliedAdmin(admin.ModelAdmin):
    list_display = ['user', 'job']
    list_per_page = 10
    
admin.site.register(Job, JobAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(SavedJobs, SavedAdmin)
admin.site.register(AppliedJobs, AppliedAdmin)