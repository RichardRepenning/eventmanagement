# This file contains the urls connected with the views.py funtion

from django.urls import path
from . import views

urlpatterns = [
  path('', views.main, name='main'),
  path('events/', views.events, name='events'),
  path('events/<slug:slug>/', views.event_detail, name='event_detail'),
  path('testing/', views.testing, name='testing'),
  path('profile', views.profile, name='profile'),
  path('profile/update', views.update_profile, name='update_profile'),
  path('signup/',views.sign_up, name='signup')
]