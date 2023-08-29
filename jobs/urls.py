from django.urls import path, include
from . import views

urlpatterns=[
     path('', views.Jobs, name='jobs'),
     path('job/<int:id>/',views.job_detail, name='job_detail'),
     path('post_job/',views.post_job, name='post_job'),
     #path('favourite_jobs/',views.favourite, name='favourite_jobs'),   
     path('relevant_jobs/', views.intelligent_search, name='intelligent-search'),
     path('job/<int:job_id>/apply/', views.apply_job, name='apply-job'),
     path('job/<int:job_id>/save/', views.save_job, name='save-job'),
     path('saved_job_list/', views.saved_jobs, name='saved-jobs'),
     path('applied_job_list/', views.applied_jobs, name='applied-jobs'),
     path('job/<int:job_id>/remove/', views.remove_job, name='remove-job'),
     
     path('sectors/', views.sectors, name='sectors'),
     path('sectors/<int:id>/',views.sector_detail, name='sectors_detail'),
     #Tag
     path('jobs/tag/<slug:tag_slug>/', views.tag_list, name='tags'),
]