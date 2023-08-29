from django.contrib import admin
from .models import LFP, EmploymentAndUnemployment

class LFPAdmin(admin.ModelAdmin):
    list_display = ['content']
    list_per_page = 10
    
class EmploymentAndUnemploymentAdmin(admin.ModelAdmin):
    list_display = ['content']
    list_per_page = 10


admin.site.register(LFP, LFPAdmin)
admin.site.register(EmploymentAndUnemployment, EmploymentAndUnemploymentAdmin)
