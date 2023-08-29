from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('labour-force-participation-rate/', views.lfp, name='labour-force-participation-rate'),
    path('employment-and-unemployment-rate/', views.employment_and_unemployment, name='employment-and-unemployment-rate'),
    
    #Tag
     path('jobs/tag/<slug:tag_slug>/', views.tag_list, name='tags'),
]