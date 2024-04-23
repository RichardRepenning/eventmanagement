from django.urls import path
from . import views

urlpatterns = [
  path('', views.main, name='main'),
  path("events/", views.events, name="events"),
  path('testing/', views.testing, name='testing'),
  path('signup/', views.signup, name='signup'),
  path('account/', views.account, name='account'),
]