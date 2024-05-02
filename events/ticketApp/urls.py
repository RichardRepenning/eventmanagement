# This file contains the urls connected with the views.py funtion

from django.urls import path
from . import views

urlpatterns = [
  path('', views.main, name='main'),
  path('events/', views.events, name='events'),
  path('testing/', views.testing, name='testing'),
  path('profile', views.profile, name='profile'),
  path('signup/',views.sign_up, name='signup')
]