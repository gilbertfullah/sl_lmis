from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('jobseeker_registeration/',views.JobSeekerRegister, name='jobseeker_register'),
     path('company_registeration/',views.CompanyRegister, name='company_register'),
     path('goverment_registeration/',views.GovernmentRegister, name='government_register'),
     path('login/', auth_views.LoginView.as_view(template_name='signin.html'), name='login'),
     path('logout/', views.logout_view, name='logout'),
     path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
     path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="reset_password_done"),
     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
     path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),
     
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
     
     path('profile/edit/', views.JobSeekerWizardView.as_view(), name='wizard_step1'),
     path('profile/edit/', views.JobSeekerWizardView.as_view(), name='wizard_step2'),
     path('profile/edit/', views.JobSeekerWizardView.as_view(), name='wizard_step3'),
     path('profile/edit/', views.JobSeekerWizardView.as_view(), name='wizard_step4'),
     path('profile/edit/', views.JobSeekerWizardView.as_view(), name='wizard_step5'),
     
     #dashboard
     path('jobseeker_dashboard/', views.jobseeker_dashboard, name='jobseeker_dashboard'),
] 