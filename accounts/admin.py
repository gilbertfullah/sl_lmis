from django.contrib import admin
from .models import User, JobSeeker, Company, Government, Skill
from django.utils.html import format_html

class UserAdmin(admin.ModelAdmin):
    list_filter = ['username']
    list_display = ['username', 'first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name', 'username']
    list_per_page = 10

class JobSeekerAdmin(admin.ModelAdmin):
    list_filter = ['first_name', 'last_name', 'username', 'email', 'status']
    list_display = ['name', 'username', 'email', 'gender', 'location', 'profession', 'status', '_']
    search_fields = ['first_name', 'last_name', 'username', 'email', 'status']
    list_per_page = 10
    
    #Method to change the icons
    def _(self, obj):
        if obj.status == "Approved":
            return True
        elif obj.status == "Pending":
            return None
        else:
            return False
    _.boolean = True
    
    # Function to color the tex
    def status(self, obj):
        if obj.status == "Approved":
            color = '#28a745'
        elif obj.status == "Pending":
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.status))
    status.allow_tags = True
    
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'email', 'region', 'sector', 'address', 'status']
    search_fields = ['company_name', 'email', 'sector', 'address']
    list_per_page = 10
    
     #Method to change the icons
    def _(self, obj):
        if obj.status == "Approved":
            return True
        elif obj.status == "Pending":
            return None
        else:
            return False
    _.boolean = True
    
    # Function to color the tex
    def status(self, obj):
        if obj.status == "Approved":
            color = '#28a745'
        elif obj.status == "Pending":
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.status))
    status.allow_tags = True
    
class GovernmentAdmin(admin.ModelAdmin):
    list_display = ['government_institution_name', 'email', 'region', 'sector', 'created_at']
    search_fields = ['government_institution_name', 'email', 'sector']
    list_per_page = 10
 
    
admin.site.register(User, UserAdmin)
admin.site.register(JobSeeker, JobSeekerAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Government, GovernmentAdmin)
admin.site.register(Skill)




