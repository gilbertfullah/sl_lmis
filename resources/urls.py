from django.urls import path, include
from . import views

urlpatterns=[
     #path('', views.resources, name='resources'),
     path('resource_list/', views.resource_list, name='resource_list'),
]