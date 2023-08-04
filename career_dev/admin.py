from django.contrib import admin
from .models import Institution

class InstitutionAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ['name']
    list_per_page = 10

admin.site.register(Institution, InstitutionAdmin)