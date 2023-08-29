from django.urls import path
from . import views

urlpatterns = [
    path('', views.lmi, name="lmi"),
    path('industrial-relations/', views.industrial_relations, name='industrial_relations'),
    path('employment-statistics/', views.employment_statistics, name='employment_statistics'),
    
] 
