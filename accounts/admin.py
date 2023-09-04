from django.contrib import admin
from .models import User, JobSeeker, Employer, Government
from django.utils.html import format_html

class UserAdmin(admin.ModelAdmin):
    list_filter = ['username']
    list_display = ['username', 'first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name', 'username']
    list_per_page = 10

class JobSeekerAdmin(admin.ModelAdmin):
    list_filter = ['first_name', 'last_name', 'username', 'email']
    list_display = ['name', 'username', 'email', 'gender', 'district', 'profession', 'employment_status']
    search_fields = ['first_name', 'last_name', 'username', 'email']
    list_per_page = 10
    
class EmployerAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'email', 'district', 'sector', 'address']
    search_fields = ['company_name', 'email', 'sector', 'address']
    list_per_page = 10
    
class GovernmentAdmin(admin.ModelAdmin):
    list_display = ['institution_name', 'email', 'district', 'sector', 'created_at']
    search_fields = ['institution_name', 'email', 'sector']
    list_per_page = 10
 
    
admin.site.register(User, UserAdmin)
admin.site.register(JobSeeker, JobSeekerAdmin)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(Government, GovernmentAdmin)



