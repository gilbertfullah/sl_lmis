from django.urls import path, include
from . import views

urlpatterns=[
     path('', views.Jobs, name='jobs'),
     path('job/<int:job_id>/', views.job_detail, name='job_detail'),
     path('post_job/',views.post_job, name='post_job'),
     #path('favourite_jobs/',views.favourite, name='favourite_jobs'),   
     #path('relevant_jobs/', views.intelligent_search, name='intelligent-search'),
     #path('job/<int:job_id>/apply/', views.apply_job, name='apply-job'),
     path('job/<int:id>/apply/', views.apply_job, name='apply_job'),
     
     #save jobs
     path('save_job/<int:job_id>/', views.save_job, name='save_job'),
     path('unsave_job/<int:job_id>/', views.unsave_job, name='unsave_job'),
     path('remove_saved_job/<int:saved_job_id>/', views.remove_saved_job, name='remove_saved_job'),
     
     path('application_success', views.application_success, name="application_success"),
     
     # Apply Jobs
     path('apply/<int:job_seeker_id>/<int:job_id>/', views.apply_job, name='apply_for_job'),
     path('application_form', views.application_form, name="application_form"),
     #path('apply/<int:job_id>/', views.JobApplicationWizardView.as_view(), name='apply_for_job'),
     #path('job_application_wizard/', views.JobApplicationWizardView.as_view(), name='job_application_wizard'),
     path('apply_job/<int:id>/', views.apply_job, name='apply_job'),
     path('applied_job_list/', views.applied_jobs, name='applied-jobs'),
     path('job/<int:job_id>/remove/', views.remove_job, name='remove-job'),
     #path('application-success/<int:id>/', views.application_success, name='application_success'),
     
     path('search_jobs/', views.job_search, name='job_search_list'),
     
     path('sectors/', views.sectors, name='sectors'),
     path('sectors/<int:id>/',views.sector_detail, name='sectors_detail'),
     #Tag
     path('jobs/tag/<slug:tag_slug>/', views.tag_list, name='tags'),
]