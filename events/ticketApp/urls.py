from django.urls import path
from . import views

urlpatterns = [
  path('', views.main, name='main'),
  path("events/", views.events, name="events"),
  path('testing/', views.testing, name='testing'),
]