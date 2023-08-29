from django.urls import path, include
from . import views

urlpatterns=[
     #path('', views.resources, name='resources'),
     path('download_list/', views.download_list, name='download_list'),
     path('labour-laws/', views.labourlaws, name='labour-laws'),
     path('policies-and-regulations/', views.policy_and_regulation, name='policies-and-regulations'),
     path('reports-and-surveys/', views.report_and_survey, name='reports-and-surveys'),
]