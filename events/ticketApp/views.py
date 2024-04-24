from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Event
from .forms import SignupForm

def events(request):
  # Create events Object with all values of Event model
  events = Event.objects.all().values()
  # Load events template
  template = loader.get_template('events.html')
  # Create an object containing the events object
  context = {
    'events': events,
  }
  # Send object to the template
  return HttpResponse(template.render(context, request))


def main(request):
  return render(request, 'index.html')

# Function for testing different aspects of Django
# without breaking main project
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'genres': ['Techno', 'Rock', 'Pop']
  }
  return HttpResponse(template.render(context, request))