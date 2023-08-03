from django.urls import path, include
from . import views

urlpatterns=[
     #path('resources/', views., name='resources'),
     path('resources/resource_list/', views.resource_list, name='resource_list'),
]