from django.urls import path
from . import views

urlpatterns=[
     path('about/',views.about, name='about'),
     path('contact_us/',views.contact, name='contact_us'),
] 