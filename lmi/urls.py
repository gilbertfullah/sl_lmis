from django.urls import path
from . import views

urlpatterns = [
    path('', views.lmi, name="labour-supply"),
    path('employment/', views.employment, name="employment"),
    path('unemployment/', views.unemployment, name="unemployment"),
    path('employer_insight/', views.employer_insight, name="employer-insight"),
    path('recruitment_insight/', views.recruitment_insight, name="recruitment-insight"),
    path('industrial-relations/', views.industrial_relations, name='industrial_relations'),
    path('employment-statistics/', views.employment_statistics, name='employment_statistics'),
    path('download/', views.download_file),
    
] 
