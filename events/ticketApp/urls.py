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
  path('profile/tickets', views.tickets, name='tickets'),
  path('profile/ticket/<str:ticket_id>/cancel', views.cancel_ticket, name='cancel_ticket'),
  path('signup/', views.sign_up, name='signup'),

  path('checkout/<str:event_id>', views.checkout, name='checkout'),
  path('checkout/payment/<str:event_id>', views.payment, name='payment'),
]
