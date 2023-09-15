from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from . import views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('jobseeker_registeration/',views.JobSeekerRegister, name='jobseeker_register'),
     path('company_registeration/',views.CompanyRegister, name='company_register'),
     path('goverment_registeration/',views.GovernmentRegister, name='government_register'),
     
     path('login/', LoginView.as_view(template_name='signin.html'), name='login'),
     path('logout/', views.logout_view, name='logout'),
     
     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
     
     path('employers/', views.employer, name="employers"),
     path('employer/job-listings/<int:employer_id>/', views.employer_job_listings, name='employer_job_listings'),
     path('employer/<int:employer_id>/', views.employer_details, name='employer_details'),
     
     path('jobseeker/profile/<int:id>/', views.jobseeker_profile, name='jobseeker_profile'),
     path('jobseeker/edit_profile/<int:id>/', views.edit_jobseeker_profile, name='edit_jobseeker_profile'),
     #path('profile/edit/', views.JobSeekerWizardView.as_view(), name='profile-edit'),
     path('profile/<int:user_id>', views.jobseeker_profile_view, name='profile-view'),
     path('introduction/', views.jobseeker_details, name='detail-candidates'),
     path('delete_skills/', views.delete_skill, name='skill-delete'),#path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     
     #dashboard
     path('jobseeker_dashboard/', views.jobseeker_dashboard, name='jobseeker_dashboard'),
     path('employer_dashboard/', views.employer_dashboard, name='employer_dashboard'),
     #path('gov_dashboard/', views.gov_dashboard, name='gov_dashboard'),
     path('default_dashboard/', views.default_dashboard, name='default_dashboard'), 
] 