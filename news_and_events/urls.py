from django.urls import path, include
from . import views

urlpatterns=[
     path('', views.news_and_events, name='news_and_events'),
     path('news/<int:news_id>/', views.news_and_event_detail, name='news_and_event_detail'),
]