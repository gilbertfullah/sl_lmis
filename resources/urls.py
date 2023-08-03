from django.urls import path, include
from . import views

urlpatterns=[
     #path('', views.resources, name='resources'),
     path('download_list/', views.download_list, name='download_list'),
     path('download_list/<int:document_id>/', views.download_document, name='download_document'),
]