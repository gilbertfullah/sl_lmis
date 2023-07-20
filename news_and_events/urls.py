from django.urls import path, include
from . import views

urlpatterns=[
     path('', views.news_and_events, name='news_and_events'),
]