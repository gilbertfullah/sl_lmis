from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('', views.employment_rate, name='employment-rate'),
    path('', views.unemployment_rate, name='unemployment-rate'),

]